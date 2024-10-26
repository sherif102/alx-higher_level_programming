#!/usr/bin/python3
"""
Module: 100-my_int.py
Author: Sheriff Abdulfatai
"""


class MyInt(int):
    """ MyInt class inheriting from int """
    def __init__(self, num):
        """ initialization """
        super().__int__()

    def __eq__(self, value):
        """ eq inverted """
        return super().__ne__(value)

    def __ne__(self, value):
        """ ne inverted """
        return super().__eq__(value)
