#!/usr/bin/python3
"""
Module: 100-append_after.py
Author: Sheriff Abdulfatai
"""


def append_after(filename="", search_string="", new_string=""):
    """ append text after the specified string """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as file:
        file.write(text)