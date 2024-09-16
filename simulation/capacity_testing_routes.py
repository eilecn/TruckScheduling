import numpy as np
import pandas as pd
from linear_program.load_data import load_historic_data


def test_daily_route(routes, demand=None, weekday='Mon-Fri', adjust_factor=1, time_per_pallet=1 / 6):
    """
    Sort default route into routes meeting the 20 pallets constraint and route that fail to meet this constraint.
    Args:
        routes: List of lists containing the default optimum route. (Mon-Fri/Sat)
        demand: Dataframe of store demand from bootstrapping or None for nothing passed in.
        weekday: String to determine the day of the week.('Mon-Fri'/'Sat')
        adjust_factor: float representing the traffic adjustment factor.
        time_per_pallet: float representing the time needed to unload one pallet.
    Returns:
        routes_passed: List of list containing the routes meeting the 20 pallets constraint.
        routes_failed: List of list containing the routes that fail to meet the 20 pallets constraint.
        routes_overtime: List of float representing overtime occurrences.
    """

    # load the historical demand and duration between store data.
    if demand is None:
        demand, duration = load_historic_data()
    else:
        dummy, duration = load_historic_data()

    # Some initial parameters
    routes_passed = []
    routes_failed = []
    routes_overtime = []
    time_this_route = 0.
    demand_this_route = 0.
    previous_store = ''
    counter = 0

    # Goes through all route in list and all store in routes
    for index in range(len(routes)):
        for store in routes[index]:

            # Skip the first route element and store it as previous store
            if (store == 'Distribution Centre Auckland') and (counter == 0):
                previous_store = store
                counter = 1

            # add the travel time from previous store to current store.
            else:
                time_this_route += duration.loc[(duration['From'] == previous_store) & (duration['To'] == store)]['Time (Hours)'].values[0] * adjust_factor
                previous_store = store

                # Add the pallet unloading time for stores
                if store != 'Distribution Centre Auckland':
                    time_this_route += round(demand.loc[demand['Store'] == store][weekday].values[0]) * time_per_pallet
                    if round(demand.loc[demand['Store'] == store][weekday].values[0]) == 0:
                        time_this_route = 0
                        break

                # Add the pallet unloading time for stores
                if store != 'Distribution Centre Auckland':
                    demand_this_route += round(demand.loc[demand['Store'] == store][weekday].values[0])

        # Add cost to the list and reset parameters
        if 0 <= demand_this_route <= 20:
            routes_passed.append(routes[index])
        else:
            routes_failed.append(routes[index])
        routes_overtime.append(time_this_route - 4 if time_this_route > 4 else 0)

        time_this_route = 0.
        demand_this_route = 0.
        previous_store = ''
        counter = 0

    # return the completed list
    return routes_passed, routes_failed, routes_overtime


def break_route_into_two(routes_failed):
    """
    Turn routes that exceed 20 pallet per truck constraint into 2 routes.
    (one route visit must be below 20 pallet constraint.)
    Args:
        routes_failed: list of lists containing the routes that exceed 20 pallet constraint.
    Returns:
        new_routes: list of lists containing the routes separated into two routes.
    """
    # Start with a empty list
    new_routes = []

    # Goes through all routes failed and separate route into two routes.
    if len(routes_failed) != 0:
        for route in routes_failed:
            extra_store = route.pop(-2)
            new_routes.append(route)
            new_routes.append(['Distribution Centre Auckland', extra_store, 'Distribution Centre Auckland'])

    return new_routes
