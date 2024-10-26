#!/usr/bin/python3
"""
Module: 8-rectangle.py
Author: Sheriff Abdulfatai
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class inherited from BaseGeometry """
    def __init__(self, width, height):
        """ initialization """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
