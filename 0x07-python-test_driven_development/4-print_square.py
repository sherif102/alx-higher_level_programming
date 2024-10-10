#!/usr/bin/python3
"""
Module: 4-print_square
Author: Sheriff Abdulfatai
"""


def print_square(size):
    """ prints a square of 'size' """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * round(size - 1), end='')
        print('#')
