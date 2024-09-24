#!/usr/bin/python3
def weight_average(my_list=[]):
    items = 0
    average = 0
    for item in my_list:
        items += item[0] * item[1]
        average += item[1]
    return items / average