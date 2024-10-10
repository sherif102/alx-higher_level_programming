#!/usr/bin/python3
"""
Module: 2-matrix_divided
Author: Sheriff Abdulfatai
"""


def matrix_divided(matrix, div):
    """ divides a matrix by a divisor """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if len(matrix) != 0:
        if not isinstance(matrix[0], list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        row = len(matrix[0])
        for m in matrix:
            for i in m:
                if not isinstance(i, (int, float)):
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
            if len(m) != row:
                raise TypeError("Each row of the matrix must "
                                "have the same size")
    return [[round(i / div, 2) for i in m] for m in matrix]
