#!/usr/bin/python3
"""
Module: 0-add_integer
Author: Sheriff Abdulfatai
"""


def add_integer(a, b=98):
    """ adds two integer value together """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
