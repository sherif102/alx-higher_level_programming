#!/usr/bin/python3
"""
Module: 3-say_my_name
Author: Sheriff Abdulfatai
"""


def say_my_name(first_name, last_name=""):
    """ prints the full_name """
    if first_name is None:
        first_name = "(null)"
    if last_name is None:
        last_name = "(null)"

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
