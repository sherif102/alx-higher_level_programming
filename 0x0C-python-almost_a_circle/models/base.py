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
