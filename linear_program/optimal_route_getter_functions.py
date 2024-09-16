import numpy as np
import pandas as pd
from mixed_integer_program import return_optimum_route
from load_data import load_generated_routes


def getRouteweekday():
    weekday, weekend = load_generated_routes()
    route, cost, index = return_optimum_route(weekday)
    return route


def getRouteweekend():
    weekday, weekend = load_generated_routes()
    route, cost, index = return_optimum_route(weekend)
    return route
