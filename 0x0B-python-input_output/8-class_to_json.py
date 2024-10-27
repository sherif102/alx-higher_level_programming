#!/usr/bin/python3
"""
Module: 8-class_to_json.py
Author: Sheriff Abdulfatai
"""


def class_to_json(obj):
    """ generate a dictionary representation of an object data struction """
    data = obj.__dict__
    result = {}
    for x in data:
        result[x] = data[x]

    return result
