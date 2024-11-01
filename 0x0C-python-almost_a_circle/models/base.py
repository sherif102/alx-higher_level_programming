#!/usr/bin/python3
"""
Module: base.py
Author: Shriff Abdulfatai
"""


class Base:
    """ defines the id of every object """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ generate dictionary repersentation of a list of dictionaries """
        import json

        result = []

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        for x in list_dictionaries:
            y = json.dumps(x)
            result.append(y)
        return result