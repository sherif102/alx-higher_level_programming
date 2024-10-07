#!/usr/bin/python3
""" This module defines a class type - square - with a private attribute - size - """
class Square:
    """ A class with attribute - size - created at the time of instantiation """
    def __init__(self, size):
        """ Initialization of -size- attribute """
        self.__size = size
