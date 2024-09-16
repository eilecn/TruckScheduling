import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

"""
INITIAL ADMIN
"""
# Random seed generation for consistency - good random seed is 22
random.seed(22)

# To change number of groups
number_points = 5

# Read in dataframe and allocates variables
df = pd.read_csv('../data/WoolworthsLocations.csv')
longitude = df['Long']
latitude = df['Lat']

# Gives range for random point allocation
longitude_range = [min(longitude), max(longitude)]
latitude_range = [min(latitude), max(latitude)]


""""
ALL HELPER FUNCTIONS TO CALL IN MAIN LOOP
"""


def generate_points(value_range):
    """
    Generates random points in range
    Returns random points
    """
    random_list = [0] * number_points
    difference = value_range[1] - value_range[0]

    for i in range(number_points):
        random_value = random.random()
        random_list[i] = random_value * difference + value_range[0]

    return random_list


def minimum_difference(data_points, centroid_list):
    """
    Governing function for calculating the centroid each point is closest to
    No returns but edits aspects in datapoints objects
    """
    for j in range(65):
        long = data_points[j].longitude
        lat = data_points[j].latitude
        min_difference = 9999999

        for i in range(number_points):
            current_difference = np.sqrt((centroid_list[i].longitude - long) ** 2 + (centroid_list[i].latitude - lat) ** 2)
            if current_difference < min_difference:
                min_difference = current_difference
                index = i

        data_points[j].closest_centroid = centroid_list[index].identifier


def test_if_stop(array):
    """
    Returns True if all centroids have not moved; otherwise, False.
    """
    for i in range(number_points):
        long_dif = array[i].longitude - (array[i].prevlong or 0)
        lat_dif = array[i].latitude - (array[i].prevlat or 0)

        if long_dif != 0 or lat_dif != 0:
            return False
    return True


def centroid_new_average(centroid, data):
    """
    Calculates new average for centroid by averaging points
    No returns but edits aspects in centroid objects
    """
    for i in range(number_points):
        num_close_points = 0
        long_total = 0
        lat_total = 0
        for j in range(65):
            if centroid[i].identifier == data[j].closest_centroid:
                long_total += data[j].longitude
                lat_total += data[j].latitude
                num_close_points += 1

        centroid[i].prevlong = centroid[i].longitude
        centroid[i].prevlat = centroid[i].latitude
        if num_close_points != 0:
            centroid[i].longitude = long_total / num_close_points
            centroid[i].latitude = lat_total / num_close_points


def graph_points():
    """
    Graphs data and organises it to be cute
    Inspired by ChatGPT but rest of file was written with no input
    Can graph up to 32 groups
    """
    colors = ['red', 'orange', 'green', 'blue', 'purple', 'red', 'orange', 'green', 'blue', 'purple', 'red', 'orange', 'green', 'blue', 'purple', 'red', 'orange', 'green', 'blue', 'purple', 'red', 'orange', 'green', 'blue', 'purple', 'red', 'orange', 'green', 'blue', 'purple', 'blue', 'purple']
    point_colours = []

    for point in points:
        for i in range(number_points):
            if point.closest_centroid == centroids[i].identifier:
                point_colours.append(colors[i])
                break

    plt.scatter([point.longitude for point in points], [point.latitude for point in points], color=point_colours)
    plt.scatter(centroid_longitude, centroid_latitude, color='black', marker='X')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Location')
    plt.show()

"""
INITIALISATION OF CLASSES
"""


class Centroids:
    def __init__(self, x, y):
        self.identifier = random.random() * 100
        self.longitude = x
        self.latitude = y
        self.prevlat = None
        self.prevlong = None
        self.stop = False


class Coordinates:
    def __init__(self, x, y):
        self.longitude = x
        self.latitude = y
        self.closest_centroid = None
        self.group = None


"""
GENERATION OF RANDOM POINTS
"""

longitude_list = generate_points(longitude_range)
latitude_list = generate_points(latitude_range)

"""
IMPLEMENTATION OF CLASSES
"""
points = [0] * 65
for i in range(65):
    points[i] = Coordinates(longitude[i], latitude[i])

centroids = [0] * number_points

for i in range(number_points):
    centroids[i] = Centroids(longitude_list[i], latitude_list[i])


"""
GOVERNING LOOP
"""
stop = False
while stop is False:
    minimum_difference(points, centroids)
    centroid_new_average(centroids, points)
    stop = test_if_stop(centroids)


"""
ALLOCATION OF GROUPS TO POINTS AND ALTERING DATAFRAME TO INCLUDE THIS
"""
centroid_longitude = [0] * number_points
centroid_latitude = [0] * number_points
identifiers = [0] * number_points

for i in range(number_points):
    centroid_longitude[i] = centroids[i].longitude
    centroid_latitude[i] = centroids[i].latitude
    identifiers[i] = centroids[i].identifier

labels = []
grouped_stores = [0] * 65
for i in range(1, number_points + 1):
    labels.append(f"Group {i}")

for j in range(65):
    for i in range(number_points):
        if points[j].closest_centroid == identifiers[i]:
            grouped_stores[j] = labels[i]

df['Group'] = grouped_stores


"""
Graphs the points as different colors *Commented out for normal use*
"""
#graph_points()

# Function to return dataframe into other files

def return_df():
    return df