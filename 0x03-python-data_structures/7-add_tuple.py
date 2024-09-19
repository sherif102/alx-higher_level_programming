#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        a, c = tuple_a[0], 0
    if len(tuple_b) == 1:
        b, d = tuple_b[0], 0
    if len(tuple_a) == 0:
        a, c = 0, 0
    if len(tuple_b) == 0:
        b, d = 0, 0

    if len(tuple_a) > 1:
        a, c = tuple_a[0], tuple_a[1]
    if len(tuple_b) > 1:
        b, d = tuple_b[0], tuple_b[1]

    result = (a + b, c + d)
    return result
