#!/usr/bin/python3
"""
Module: 101-add_attribute.py
Author: Sheriff Abdulfatai
"""


def add_attribute(obj, att, value):
    """ adds new attribute and value to a class """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
