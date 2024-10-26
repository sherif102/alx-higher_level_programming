#!/usr/bin/python3
"""
Module: 3-to_json_string.py
Author: Sheriff Abdulfatai
"""


def to_json_string(my_obj):
    """ send data to json string """
    import json
    return json.dumps(my_obj)
