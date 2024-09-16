# Eileen made this! :D

import pandas as pd
from route_generation.cluster_stores import return_df


# Getting the dataframe from cluster_stores file and removing the distribution centre row
df = return_df()
df = df.drop([64])

# Creating a pandas dataframe from demand estimation
demand_df = pd.read_csv('../data/Demand_Estimation.csv')

# Adding demand estimations for each store to the dataframe
df.loc[:, "WeekdayDemand"] = demand_df[['Mon-Fri']]
df.loc[:, "SaturdayDemand"] = demand_df[['Sat']]

# Splitting the dataframe into each cluster group
grouped = df.groupby(df.Group)
df1 = grouped.get_group('Group 1')
df2 = grouped.get_group('Group 2')
df3 = grouped.get_group('Group 3')
df4 = grouped.get_group('Group 4')
df5 = grouped.get_group('Group 5')

# Adding the dataframes to a list 
groups = [df1, df2, df3, df4, df5]

# Initialising dictionary for routes in each cluster
routes1 = {}
routes2 = {}
routes3 = {}
routes4 = {}
routes5 = {}

# Add to list for loop convenience
route_dictionaries = [routes1, routes2, routes3, routes4, routes5]

# Count to keep track of number of routes generated
count = 1

# Defining attributes of each route
class Route:
    def __init__(self, Type1, Location1, Type2, Location2, Type3, Location3, Total_Demand):
        self.Type1 = Type1
        self.Location1 = Location1
        self.Type2 = Type2
        self.Location2 = Location2
        self.Type3 = Type3
        self.Location3 = Location3
        self.Total_Demand = Total_Demand
    
    # For printing
    def __repr__(self):
        return f'Location 1: {self.Type1} {self.Location1}, Location 2: {self.Type2} {self.Location2}, Location 3: {self.Type3} {self.Location3}, Total_Demand: {self.Total_Demand}\n'

# Looping over each cluster
for i in range(len(groups)):

    # Accessing each cluster's dataframe from list
    df = groups[i]

    # Looping over each store in each cluster
    for j in range(0, len(groups[i])):
         
         # Finding the demand of the first store by accessing the cluster dataframe
         first_store_demand = round(df.iat[j, df.columns.get_loc('WeekdayDemand')])

         # Checking if demand does not exceed capacity of truck
         if first_store_demand <= 20 and first_store_demand > 0:
                 
                 # Generate route object and add to corresponding dictionary depending on cluster number 
                 route_dictionaries[i]['generated_route' + str(count)] = Route(df.iat[j, df.columns.get_loc('Type')], df.iat[j, df.columns.get_loc('Location')], None, None, None, None, first_store_demand)
                 
                 # Increment to keep track of number of generated routes
                 count += 1

         # Breaking loop if iterating over last store in dataframe, not possible to have another store after
         if j == len(groups[i]) - 1:
             break
             
         # Looping over second store 
         for k in range(0, len(groups[i])):
             if (k != j):
             
                # Finding the demand of the second store by accessing the cluster dataframe
                second_store_demand = round(df.iat[k, df.columns.get_loc('WeekdayDemand')])

                # Checking if total demand is less than truck capacity
                if first_store_demand + second_store_demand <= 20 and second_store_demand > 0:
                    
                    # Generate route object and add to corresponding dictionary depending on cluster number 
                    route_dictionaries[i]['generated_route' + str(count)] = Route(df.iat[j, df.columns.get_loc('Type')], df.iat[j, df.columns.get_loc('Location')], df.iat[k, df.columns.get_loc('Type')], df.iat[k, df.columns.get_loc('Location')], None, None, first_store_demand + second_store_demand)
                    
                    # Increment to keep track of number of generated routes
                    count += 1

                # Breaking loop if iterating over last store in dataframe, not possible to have another store after
                if k == len(groups[i]) - 1:
                    break

                
                # Looping over third store
                for l in range(0, len(groups[i])):

                    if (l != k and l != j and k != j):
                    
                        # Finding the demand of the third store by accessing the cluster dataframe
                        third_store_demand = round(df.iat[l, df.columns.get_loc('WeekdayDemand')])

                        # Checking if total demand is less than truck capacity
                        if first_store_demand + second_store_demand + third_store_demand <= 20 and third_store_demand > 0:
                            
                            # Generate route object and add to corresponding dictionary depending on cluster number 
                            route_dictionaries[i]['generated_route' + str(count)] = Route(df.iat[j, df.columns.get_loc('Type')], df.iat[j, df.columns.get_loc('Location')], df.iat[k, df.columns.get_loc('Type')], df.iat[k, df.columns.get_loc('Location')], df.iat[l, df.columns.get_loc('Type')], df.iat[l, df.columns.get_loc('Location')], first_store_demand + second_store_demand + third_store_demand)
                            
                            # Increment to keep track of number of generated routes
                            count += 1

# To access dictionary in other files
def get_weekday_routes():
    return routes1, routes2, routes3, routes4, routes5

# print(routes2)
# print(routes4)
