#!/usr/bin/python3
"""
Module: 4-from_json_string.py
Author: Sheriff Abdulfatai
"""


def from_json_string(my_str):
    """ generate executable from json string """
    import json
    json.loads(my_str)
