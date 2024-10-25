#!/usr/bin/python3
"""
Module: 4-inherits_from.py
Author: Sheriff Abdulfatai
"""


def inherits_from(obj, a_class):
    """ check if obj inherits from a_class """
    return isinstance(obj, a_class) and type(obj) is not a_class
