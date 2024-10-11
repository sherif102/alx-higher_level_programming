#!/usr/bin/python3
# Module: 100-matrix_mul
# Author: Sheriff Abdulfatai
""" Multiply two matrices """


def matrix_mul(m_a, m_b):
    """ multiplies m_a and m_b matrices """

    result = []

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    row = len(m_a[0])
    col = len(m_b)

    if row != col:
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    cal = 0

    for xr in range(len(m_a[0])):
        for mbc in range(len(m_b[0])):
            if len(m_a[xr]) != len(m_a[0]):
                    raise TypeError("each row of m_a must be of the same size")
            if len(m_b[mbc]) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
            
            for xc in range(len(m_b)):
                if not isinstance(m_a[xr][xc], (int, float)):
                    raise TypeError("m_a should contain "
                                    "only integers or floats")
                if not isinstance(m_b[xc][mbc], (int, float)):
                    raise TypeError("m_b should contain "
                                    "only integers or floats")
                cal += m_a[xr][xc] * m_b[xc][mbc]
                
            res.append(cal)
            cal = 0
        result.append(res)
        res = []
    return result
