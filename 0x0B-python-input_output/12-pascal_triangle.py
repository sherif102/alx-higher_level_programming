#!/usr/bin/python3
"""
Module: 12-pascal_triangle.py
Author: Sheriff Abdulfatai
"""


def pascal_triangle(n):
    """ define pascal triangle of n size """
    def permutate(x):
        """ permutation """
        y = 1
        for i in range(1, x + 1,):
            y *= i
        return y

    def combine(n, k):
        """ combination """
        return permutate(n) // (permutate(k) * permutate(n - k))

    if n <= 0:
        return []

    result = []
    for f_number in range(n):
        data = []
        for s_number in range(f_number + 1):
            data.append(combine(f_number, s_number))
        result.append(data)
    return result
