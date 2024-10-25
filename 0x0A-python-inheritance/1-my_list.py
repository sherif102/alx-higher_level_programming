#!/usr/bin/python3
"""
Module: 1-my_list.py
Author: Sheriff Abdulfatai
"""


class MyList(list):
    """ class that inherits from 'list' class """
    def __init__(self):
        """ initializes the list """
        self.lst = []

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
