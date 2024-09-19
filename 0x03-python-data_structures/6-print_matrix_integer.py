#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mlen = len(matrix)
    i = 0
    while i < mlen:
        for j in matrix[i]:
            smlen = len(matrix[i])
            if j == matrix[i][smlen - 1]:
                print("{}".format(j))
                continue
            print("{}".format(j), end=" ")
        i += 1
