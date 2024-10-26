#!/usr/bin/python3
"""
Module: 1-write_file.py
Author: Sheriff Abdulfatai
"""


def write_file(filename="", text=""):
    """ write text to file """
    with open(filename, mode='w') as file:
        written = file.write(text)
        return written
