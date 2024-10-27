#!/usr/bin/python3
"""
Module: 2-append_write.py
Author: Sheriff Abdulfatai
"""


def append_write(filename="", text=""):
    """ append text to end of file """
    with open(filename, 'a') as file:
        appended = file.write(text)
        return appended
