import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
from linear_program.mixed_integer_program import *
from bootstrapping import generate_all_demands
from capacity_testing_routes import *

default_weekday = [['Distribution Centre Auckland', 'Woolworths Auckland City', 'Metro Albert Street', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Birkenhead', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Browns Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Glenfield', 'Woolworths Milford', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Greville Road', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Grey Lynn', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Hauraki Corner', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mairangi Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Northcote', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Ponsonby', 'Metro Herne Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Sunnynook', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Takapuna', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Papakura', 'Woolworths Papakura', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Manukau', 'FreshChoice Flat Bush', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Manukau Mall', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Manurewa', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Blockhouse Bay', 'FreshChoice Titirangi', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Henderson', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Lincoln Road', 'FreshChoice Ranui', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Lynnmall', 'FreshChoice Glen Eden', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Northwest', 'Woolworths Hobsonville', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Pt Chevalier', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Papatoetoe', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Te Atatu North', 'SuperValue Avondale', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Te Atatu South', 'FreshChoice Palomino', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Westgate', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Otahuhu', 'Woolworths Botany Downs', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Roselands', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Highland Park', 'FreshChoice Half Moon Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Howick', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Meadowbank', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Meadowlands', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mt Wellington', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Pakuranga', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths St Johns', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Takanini', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Epsom', 'Woolworths Greenlane', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Mangere Bridge', 'Woolworths Onehunga', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Airport', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Waiata Shores', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mangere East', 'Woolworths Mangere Mall', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mt Eden', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mt Roskill', 'Woolworths Three Kings', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Newmarket', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths St Lukes', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Metro Halsey Street', 'Woolworths Auckland Victoria Street West', 'Distribution Centre Auckland']]

default_sat = [['Distribution Centre Auckland', 'Woolworths Howick', 'Woolworths Meadowlands', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Meadowbank', 'Woolworths St Johns', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mt Wellington', 'Woolworths Pakuranga', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mangere East', 'Woolworths Mangere Mall', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Mt Roskill', 'Woolworths Three Kings', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Newmarket', 'Woolworths Greenlane', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Onehunga', 'Woolworths Airport', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths St Lukes', 'Woolworths Mt Eden', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Epsom', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Flat Bush', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Glen Eden', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Half Moon Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Mangere Bridge', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Otahuhu', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Palomino', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Papakura', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Ranui', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'FreshChoice Titirangi', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Metro Albert Street', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Metro Halsey Street', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Metro Herne Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'SuperValue Avondale', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Takanini', 'Woolworths Manurewa', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Auckland City', 'Woolworths Auckland Victoria Street West', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Birkenhead', 'Woolworths Northcote', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Glenfield', 'Woolworths Milford', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Greville Road', 'Woolworths Browns Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Grey Lynn', 'Woolworths Ponsonby', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Manukau Mall', 'Woolworths Manukau', 'Woolworths Papatoetoe', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Hauraki Corner', 'Woolworths Takapuna', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Sunnynook', 'Woolworths Mairangi Bay', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Blockhouse Bay', 'Woolworths Lynnmall', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Lincoln Road', 'Woolworths Henderson', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Northwest', 'Woolworths Hobsonville', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Pt Chevalier', 'Woolworths Westgate', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Te Atatu South', 'Woolworths Te Atatu North', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Papakura', 'Woolworths Roselands', 'Woolworths Waiata Shores', 'Distribution Centre Auckland'], ['Distribution Centre Auckland', 'Woolworths Highland Park', 'Woolworths Botany Downs', 'Distribution Centre Auckland']]


def simulation(default_route, number_of_runs=100, weekday='Mon-Fri'):
    """
    Run 100 days simulation based on a default route and random demand and randomly generated traffic adjusting factor.
    Args:
        default_route: List of lists containing the default optimum route. (Mon-Fri/Sat)
        number_of_runs: Integer of number of runs to be carried out.
        weekday: String to determine the day of the week.('Mon-Fri'/'Sat')
    Returns:
        simulated_cost_list: List of floats containing the cost of all simulated runs
        simulated_overtime_list: List of floats containing the overtime occurrences of all runs
        factor_list: List of floats containing the traffic factors of all runs
    """
    # Creating the list for the output
    simulated_cost_list = []
    simulated_overtime_list = []
    factor_list = []

    # Simulate number of runs and see the change in cost in vary demand and traffic.
    for i in range(number_of_runs):

        # Print current number of runs
        print(i)

        # make the condition list not empty
        routes_failed = ['Not empty']

        # create a copy of the default route to be tested in every simulation
        routes = copy.deepcopy(default_route)

        # Generate a bootstrapped demand from past historical data of individual store
        demand = generate_all_demands()

        # Test whether all routes are under 20 pallet constraint, breaking route into two if needed.
        while len(routes_failed) != 0:

            routes_passed, routes_failed, routes_overtime = test_daily_route(routes, demand, weekday=weekday)
            new_routes = break_route_into_two(routes_failed)

            if len(new_routes) != 0:
                routes = routes_passed + new_routes

        factor = max(0.7, np.random.normal(loc=1, scale=0.15))
        route, cost, index = return_optimum_route(routes_passed, demand, 'Mon-Fri', factor, daily_test=True)

        # Throw an error if not all route are used.
        if len(route) != len(routes_passed):
            raise Exception("Something went wrong and unexpected stuff happened")

        # append result into output list
        factor_list.append(factor)
        simulated_cost_list.append(cost)
        simulated_overtime_list.append(np.count_nonzero(routes_overtime))

    return simulated_cost_list, simulated_overtime_list, factor_list


def plot_simulation(simulated_cost_list, simulated_overtime_list, factor_list):
    """
    plot the simulated cost, overtime, traffic adjustment factor.
    Args:
        simulated_cost_list: List of floats containing the cost of all simulated runs
        simulated_overtime_list: List of floats containing the overtime occurrences of all runs
        factor_list: List of floats containing the traffic factors of all runs
    """
    # Create some plots and add other needed features such as labels, titles, legends.
    plt.boxplot(simulated_cost_list)
    plt.xlabel('The Run Number (Simulation/Day X)')
    plt.ylabel('Estimated Daily Cost ($NZD)')
    plt.title("Cost of The Monday-Friday Route Given a 100 Day Simulation")
    plt.show()

    plt.boxplot(simulated_overtime_list)
    plt.xlabel('The Run Number (Simulation/Day X)')
    plt.ylabel('Overtime Count (Number of Overtime)')
    plt.title("Overtime Count in The Monday-Friday Route Given a 100 Day Simulation")
    plt.show()

    plt.boxplot(factor_list)
    plt.xlabel('The Run Number (Simulation/Day X)')
    plt.ylabel('Traffic coefficient (Number of Overtime)')
    plt.title("Randomly Generated Traffic Coefficient Given a 100 Day Simulation")
    plt.show()
    return
