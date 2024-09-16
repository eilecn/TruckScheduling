from route_generation.weekday_route_generation import get_weekday_routes
from route_generation.weekend_route_generation import get_weekend_routes

weekday_routes_1, weekday_routes_2, weekday_routes_3, weekday_routes_4, weekday_routes_5 = get_weekday_routes()
weekend_routes_1, weekend_routes_2, weekend_routes_3, weekend_routes_4, weekend_routes_5 = get_weekend_routes()

weekday_list_1 = []
weekday_list_2 = []
weekday_list_3 = []
weekday_list_4 = []
weekday_list_5 = []

weekend_list_1 = []
weekend_list_2 = []
weekend_list_3 = []
weekend_list_4 = []
weekend_list_5 = []

for object in weekday_routes_1.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_1.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_1.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_1.append(new_list)


for object in weekday_routes_2.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_2.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_2.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_2.append(new_list)


for object in weekday_routes_3.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_3.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_3.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_3.append(new_list)


for object in weekday_routes_4.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_4.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_4.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_4.append(new_list)


for object in weekday_routes_5.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_5.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_5.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekday_list_5.append(new_list)


for object in weekend_routes_1.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_1.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_1.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_1.append(new_list)

for object in weekend_routes_2.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_2.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_2.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_2.append(new_list)


for object in weekend_routes_3.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_3.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_3.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_3.append(new_list)


for object in weekend_routes_4.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_4.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_4.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_4.append(new_list)


for object in weekend_routes_5.values():
    new_list = ['Distribution Centre Auckland']
    if object.Location2 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_5.append(new_list)
    elif object.Location3 is None:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_5.append(new_list)
    else:
        first_store = object.Type1 + ' ' + object.Location1
        new_list.append(first_store)
        second_store = object.Type2 + ' ' + object.Location2
        new_list.append(second_store)
        third_store = object.Type3 + ' ' + object.Location3
        new_list.append(third_store)
        new_list.append('Distribution Centre Auckland')
        weekend_list_5.append(new_list)

def get_data():
    return weekday_list_1, weekday_list_2, weekday_list_3, weekday_list_4, weekday_list_5, weekend_list_1, weekend_list_2, weekend_list_3, weekend_list_4, weekend_list_5



