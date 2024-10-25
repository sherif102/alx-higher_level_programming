#!/usr/bin/python3
"""
Module: 1-my_list.py
Author: Sheriff Abdulfatai
"""


class MyList(list):
    """ class that inherits from 'list' class """
    def __init__(self, lst=[]):
        """ initializes the list """
        self.lst = lst

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))

    def __str__(self):
        return str(self)