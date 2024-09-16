import numpy as np
import pandas as pd
from pulp import *
from mixed_integer_program.load_data import load_historic_data, load_generated_routes


def find_cost_for_routes(routes_list, demand=None, weekday='Mon-Fri', time_per_pallet=1 / 6, adjust_factor=1):
    """
    Find the corresponding distribution cost for list of routes passed in based on given distribution cost.
    Args:
        routes_list: List of list of routes.
        demand: Dataframe or None depending on whether bootstrapping of past demand are used.
        weekday: String of time of week. ('Mon-Fri'/'Sat')
        time_per_pallet: Float of time taken to unload one pallet.
        adjust_factor: Float of traffic adjusting factor.
    Returns:
        cost_list: List of float on distribution cost for routes in routes_list.
    """
    # load the historical demand and duration between store data.
    if demand is None:
        demand, duration = load_historic_data()
    else:
        dummy, duration = load_historic_data()

    # $250 per hour per truck to operate
    # $325 per hour per truck to operate in overtime
    normal_cost = 250
    overtime_cost = 325

    # Some initial parameters
    costs_list = []
    time_current_route = 0.
    previous_store = ''
    counter = 0

    # Goes through all route in list and all store in routes
    for index in range(len(routes_list)):
        for store in routes_list[index]:
            # Skip the first route element and store it as previous store
            if (store == 'Distribution Centre Auckland') and (counter == 0):
                previous_store = store
                counter = 1

            # add the travel time from previous store to current store.
            else:
                time_current_route += duration.loc[(duration['From'] == previous_store)
                                                & (duration['To'] == store)]['Time (Hours)'].values[0] * adjust_factor
                previous_store = store

                # Add the pallet unloading time for stores
                if store != 'Distribution Centre Auckland':
                    time_current_route += round(demand.loc[demand['Store'] == store][weekday].values[0]) * time_per_pallet
                    if round(demand.loc[demand['Store'] == store][weekday].values[0]) == 0:
                        time_current_route = 0
                        break

        # Add cost to the list and reset parameters
        cost_current_route = time_current_route * normal_cost + ((time_current_route - 4) * overtime_cost if time_current_route > 4 else 0)
        costs_list.append(cost_current_route)
        time_current_route = 0.
        previous_store = ''
        counter = 0

    return costs_list


def find_optimal_schedule(routes_index, routes_dict, travel_cost_dict, demand=None, daily_test=False):
    """
    Find the optimal schedule for woolworth truck scheduling using PuLP to solve the linear programming problem.
    Args:
        routes_index: List of integers on routes index
        routes_dict: Dictionary of routes on route index
        travel_cost_dict: Dictionary of travel costs on routes index.
        demand: Dataframe or None depending on whether bootstrapping of past demand are used.
        daily_test: Boolean on whether all route inputted are used (all route will be used in daily test)
    Returns:
        output_route_list: List of list containing the index of the optimum route
        output_cost: Float of the optimal cost
    """
    # load the historical demand and duration between store data.
    if demand is None:
        demand, duration = load_historic_data()
    else:
        dummy, duration = load_historic_data()

    # Some set parameters from the brief
    # $240.3846 per day,($75000 per year/ $240.3846 per working day(no sunday/52 weeks)) maintenance cost of 1 truck
    # $2300 for four hours duty (cost of increasing truck count) (~2* normal price)
    maintenance_cost = 240.3846
    add_truck_cost = 2300

    # LP formulation
    prob = LpProblem("The_Route_Scheduling_Problem", LpMinimize)

    # Creating the linear programming variables and objective function
    route_vars = LpVariable.dicts('Route', routes_index, lowBound=0, upBound=1, cat=LpInteger)
    trucks = LpVariable('Trucks', lowBound=0, upBound=24, cat=LpInteger)
    add_trucks = LpVariable('Trucks_Rented',lowBound=0, upBound=None, cat=LpInteger)

    # Objective function: minimise cost overall
    prob += lpSum([add_trucks * add_truck_cost] + [trucks * maintenance_cost]
                  + [travel_cost_dict[route] * route_vars[route] for route in routes_index])

    # All store only need to be visited once in a day
    for store in demand['Store']:
        prob += lpSum([route_vars[route] for route in routes_index if (store in routes_dict[route])]) == 1

    # Truck and routing constraint, all route have to have a truck to deliver them.
    prob += lpSum([route_vars[route] for route in routes_index if (travel_cost_dict[route] != 0)]) - (
                (2 * trucks) + add_trucks) <= 0

    # Whether to fix truck use to 24.
    prob += lpSum(trucks) == 24

    # If all routes passed in are used and we are implementing a daily test.
    if daily_test:
        for route in routes_index:
            prob += lpSum(route_vars[route]) == 1

    prob.solve(PULP_CBC_CMD(msg=0))
    print("Status:", LpStatus[prob.status])
    # for v in prob.variables():
    #     print(v.name, "=", v.varValue)
    # print("Total daily expense (accrual accounting) on distribution of pallets = $", value(prob.objective))
    output_route_list = [f'{v}'.strip('Route_') for v in prob.variables() if ((v.varValue == 1) & (f'{v}' != 'Trucks_Rented'))]
    output_cost = value(prob.objective)
    return output_route_list, output_cost


def return_actual_route(index_list, routes_dict):
    """
    Find the optimal route using the index of the route and route dictionary with the actual route.
    Args:
        index_list: List of integers on optimum route index
        routes_dict: Dictionary of routes on optimum route index
    Returns:
        actual_route: List of list containing routes on optimum route index
    """
    # creating an empty list for routes
    actual_route = []

    # Goes through all route index and add the corresponding route in the dictionary
    for element in index_list:
        actual_route.append(routes_dict[element])

    return actual_route


def return_optimum_route(routes, demand=None, week_time='Mon-Fri', factor=1, daily_test=False):
    """
    Using all above functions to find the optimal route, optimal cost and the route index of optimal route.
    Args:
        routes: List of list containing optimum route
        demand: Dataframe or None depending on whether bootstrapping of past demand are used.
        week_time: String of time of week. ('Mon-Fri'/'Sat')
        factor: Float of traffic adjusting factor.
        daily_test: Boolean on whether all route inputted are used (all route will be used in daily test)
    Returns:
        optimum_route: List of list containing optimum route.
        optimum_cost: Float of the optimum cost
        output_route_index: List of list containing the index of the optimum route
    """
    # Finding cost of all routes depending on day of week (different demand).
    if week_time == 'Mon-Fri':
        travel_cost_list = find_cost_for_routes(routes, demand, weekday='Mon-Fri', adjust_factor=factor)
    elif week_time == 'Sat':
        travel_cost_list = find_cost_for_routes(routes, demand, weekday='Sat', adjust_factor=factor)
    else:
        print("Error in week_time input")

    # Creating the route index for all route and 2 dictionaries for all route and all route cost
    routes_index = [f'{i + 1}' for i in range(len(routes))]
    routes_dict = dict(zip(routes_index, routes))
    travel_cost_dict = dict(zip(routes_index, travel_cost_list))

    # Solve the linear program and find the optimal_route, cost and index for the route.
    optimal_route_index, optimal_cost = find_optimal_schedule(routes_index, routes_dict, travel_cost_dict, demand, daily_test=daily_test)
    optimal_route = return_actual_route(optimal_route_index, routes_dict)
    return optimal_route, optimal_cost, optimal_route_index
