import numpy as np
import pandas as pd
import random


def week_data(df, store_index, weekend):

    columns = df.columns

    if weekend is True:
        data = [0] * 4
        j = 0

        for i in range(1, len(df.iloc[store_index])):
            weekday = True

            if i == 6 or i == 13 or i == 20 or i == 27:
                weekday = False

            if weekday is False:
                data[j] = df[columns[i]].iloc[store_index]

                j += 1

    else:
        data = [0] * 20
        j = 0

        for i in range(1, len(df.iloc[0])):
            weekday = True

            if i == 6 or i == 7 or i == 13 or i == 14 or i == 20 or i == 21 or i == 27 or i == 28:
                weekday = False

            if weekday is True:
                data[j] = df[columns[i]].iloc[store_index]

                j += 1

    return data


def generate_probabilities(data):
    possible_demands = list(set(data))
    demand_prob = [0] * len(possible_demands)

    for i in range(len(possible_demands)):
        demand_prob[i] = data.count(possible_demands[i]) / len(data)

    prob_series = pd.Series(data=demand_prob, index=possible_demands)

    return prob_series


def demand_gen(prob_series):

    numbers = list(prob_series.index)
    prob = prob_series.values

    demand = random.choices(numbers, prob)

    return demand[0]


def generate_all_demands():

    random.seed()
    df = pd.read_csv('../data/WoolworthsDemand2024.csv')

    # For weekdays:
    random_demand_weekday = [0] * 64
    random_demand_saturday = [0] * 64

    for i in range(64):
        data = week_data(df, i, False)
        prob_series = generate_probabilities(data)
        random_demand_weekday[i] = demand_gen(prob_series)

    # For saturdays:
    for i in range(64):
        data = week_data(df, i, True)
        prob_series = generate_probabilities(data)
        random_demand_saturday[i] = demand_gen(prob_series)

    store_names = list(df['Store'])

    data = {'Store': store_names,
            'Mon-Fri': random_demand_weekday,
            'Sat': random_demand_saturday}

    demand_df = pd.DataFrame(data)

    return demand_df
