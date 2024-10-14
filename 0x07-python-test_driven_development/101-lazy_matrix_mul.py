#!/usr/bin/python3
"""
Module: 100-lazy_matrix_mul
Author: Sheriff Abdulfatai
"""


def lazy_matrix_mul(m_a, m_b):
    import numpy as np
    """ multiplies m_a and m_b matrices with numpy """

    a = np.array(m_a)
    b = np.array(m_b)
    result = a @ b
    return result
