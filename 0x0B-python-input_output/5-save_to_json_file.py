#!/usr/bin/python3
"""
Module: 5-save_to_json_file.py
Author: Sheriff Abdulfatai
"""


def save_to_json_file(my_obj, filename):
    """ saves data to json file """
    import json
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
