#!/usr/bin/python3
"""
Module: 10-square.py
Author: Sheriff Abdulfatai
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class inherited from rectangle """
    def __init__(self, size):
        """ initialization """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ return the area of the rectangle """
        return self.__size ** 2

    def __str__(self):
        """ return teh string representation """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
