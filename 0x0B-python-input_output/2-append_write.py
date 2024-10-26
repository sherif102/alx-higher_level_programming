#!/usr/bin/python3
"""
Module: 0-read_file.py
Author: Sheriff Abdulfatai
"""


def append_write(filename="", text=""):
    """ append text to end of file """
    with open(filename, 'a') as file:
        appended = file.write(text)
        return appended
