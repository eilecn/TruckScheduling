import numpy as np
import pandas as pd
from route_generation.formatting_route_data import get_data

one_store_route = [['Distribution Centre Auckland', 'FreshChoice Epsom', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Flat Bush', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Glen Eden', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Half Moon Bay', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Mangere Bridge', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Otahuhu', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Palomino', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Papakura', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Ranui', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'FreshChoice Titirangi', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Metro Albert Street', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Metro Halsey Street', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Metro Herne Bay', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'SuperValue Avondale', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Airport', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Auckland City', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Auckland Victoria Street West',
                    'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Birkenhead', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Blockhouse Bay', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Botany Downs', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Browns Bay', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Glenfield', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Greenlane', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Greville Road', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Grey Lynn', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Hauraki Corner', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Henderson', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Highland Park', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Hobsonville', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Howick', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Lincoln Road', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Lynnmall', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Mairangi Bay', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Mangere East', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Mangere Mall', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Manukau', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Manukau Mall', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Manurewa', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Meadowbank', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Meadowlands', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Milford', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Mt Eden', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Mt Roskill', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Mt Wellington', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Newmarket', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Northcote', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Northwest', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Onehunga', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Pakuranga', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Papakura', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Papatoetoe', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Ponsonby', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Pt Chevalier', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Roselands', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths St Johns', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths St Lukes', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Sunnynook', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Takanini', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Takapuna', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Te Atatu North', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Te Atatu South', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Three Kings', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Waiata Shores', 'Distribution Centre Auckland'],
                   ['Distribution Centre Auckland', 'Woolworths Westgate', 'Distribution Centre Auckland']]

non_woolworth_route = [['Distribution Centre Auckland', 'FreshChoice Epsom', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Flat Bush', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Glen Eden', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Half Moon Bay', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Mangere Bridge', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Otahuhu', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Palomino', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Papakura', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Ranui', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'FreshChoice Titirangi', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'Metro Albert Street', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'Metro Halsey Street', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'Metro Herne Bay', 'Distribution Centre Auckland'],
                       ['Distribution Centre Auckland', 'SuperValue Avondale', 'Distribution Centre Auckland']]

def load_historic_data():
    """
    Loads historic woolworth data and returns it as a pandas dataframe.
    Returns:
        demand: pandas dataframe of historical woolworth demand
        duration: pandas dataframe of OpenStreetMap duration between woolworth stores.
    """
    # loading and preprocessing the default data from woolworth historical data.
    demand = pd.read_csv('../data/Demand_Estimation.csv')
    demand.rename(columns={'Unnamed: 0': 'Store'}, inplace=True)

    # loading and preprocessing the default data from OpenStreetMap data to travel between stores.
    duration = pd.read_csv('../data/WoolworthsDurations.csv')
    duration.rename(columns={'Unnamed: 0': 'From'}, inplace=True)
    duration = duration.melt(id_vars=['From'], var_name='To', value_name='Time (Sec)', )
    duration['Time (Sec)'] = duration['Time (Sec)'] / 3600
    duration.rename(columns={'Time (Sec)': 'Time (Hours)'}, inplace=True)

    return demand, duration


def load_generated_routes():
    """
    Loads generated routes data and returns nested list. (Need get_data() function)
    Returns:
        weekday_list: list of list containing all weekday routes.
        weekend_list: list of list containing all weekend routes.
    """
    # Non woolworth stores.
    non_woolworth = ['FreshChoice Epsom', 'FreshChoice Flat Bush', 'FreshChoice Glen Eden',
                     'FreshChoice Half Moon Bay', 'FreshChoice Mangere Bridge',
                     'FreshChoice Otahuhu', 'FreshChoice Palomino', 'FreshChoice Papakura',
                     'FreshChoice Ranui', 'FreshChoice Titirangi', 'Metro Albert Street',
                     'Metro Halsey Street', 'Metro Herne Bay', 'SuperValue Avondale']

    # Non woolworth store single store routes.
    non_woolworth_route = [['Distribution Centre Auckland', 'FreshChoice Epsom', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Flat Bush', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Glen Eden', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Half Moon Bay',
                            'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Mangere Bridge',
                            'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Otahuhu', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Palomino', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Papakura', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Ranui', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'FreshChoice Titirangi', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'Metro Albert Street', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'Metro Halsey Street', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'Metro Herne Bay', 'Distribution Centre Auckland'],
                           ['Distribution Centre Auckland', 'SuperValue Avondale', 'Distribution Centre Auckland']]

    # Obtaining the data and get the routing options for weekday and sat.
    (weekday_list_1, weekday_list_2, weekday_list_3, weekday_list_4, weekday_list_5,
     weekend_list_1, weekend_list_2, weekend_list_3, weekend_list_4, weekend_list_5) = get_data()

    # Setting weekday list and weekend list from all the routes generated.
    weekday_list = weekday_list_1 + weekday_list_2 + weekday_list_3 + weekday_list_4 + weekday_list_5
    sat_list = weekend_list_1 + weekend_list_2 + weekend_list_3 + weekend_list_4 + weekend_list_5

    # Implemented a basic test to see if all route in sat_list is possible (only woolworth store are visited).
    weekend_list = []
    counter = 0
    for element in sat_list:
        for store in non_woolworth:
            if store in element:
                counter += 1

        if counter == 0:
            weekend_list.append(element)
        counter = 0

    # append all single non woolworth store routes at the end of the list for dummy variables in linear programming.
    weekend_list = weekend_list + non_woolworth_route
    return weekday_list, weekend_list
