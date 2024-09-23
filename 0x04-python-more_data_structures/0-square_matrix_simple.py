#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for x in matrix:
        sq_matrix.append(list(map(lambda y: y ** 2, x)))
    return sq_matrix
