#!/usr/bin/python3
"""
Module: 7-base_geometry.py
Author: Sheriff Abdulfatai
"""


class BaseGeometry():
    """ the base class """
    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ valudates value """
        if not isinstance(value, int):
            raise TypeError(str(name) + " must be an integer")
        if (value <= 0):
            raise ValueError(str(name) +" must be greater than 0")
