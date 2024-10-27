#!/usr/bin/python3
"""
Module: 6-load_from_json_file.py
Author: Sheriff Abdulfatai
"""


def load_from_json_file(filename):
    """ load a json file """
    import json
    with open(filename) as file:
        loaded = json.load(file)
        return loaded
