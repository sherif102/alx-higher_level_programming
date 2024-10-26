#!/usr/bin/python3
"""
Module: 0-read_file.py
Author: Sheriff Abdulfatai
"""


def read_file(filename=""):
    """ read_file read file and print to stdout """
    with open(filename) as file:
        for line in file:
            print(line, end='')
