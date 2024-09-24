#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    value = 0
    for x, y in a_dictionary.items():
        if y >= value:
            value = y
            key = x
    return key
