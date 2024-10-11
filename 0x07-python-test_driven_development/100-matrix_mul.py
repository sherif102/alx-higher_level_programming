#!/usr/bin/python3
# Module: 100-matrix_mul
# Author: Sheriff Abdulfatai
""" Multiply two matrices """


def matrix_mul(m_a, m_b):
    """ multiplies m_a and m_b matrices

    --------------------------------------------
    # correct input
    >>> matrix_mul([[3, 1, 2], [0, 2, 1], [1, 3, 2]], [[0, 1, 1], [2, 0, 1], [1, 2, 0]])
    [[4, 7, 4], [5, 2, 2], [8, 5, 4]]

    # m_a is not a list
    >>> matrix_mul('a', [[3, 1, 2], [0, 2, 1], [1, 3, 2]])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list

    # m_b is not a list
    >>> matrix_mul([[3, 1, 2], [0, 2, 1], [1, 3, 2]], 4)
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list

    # m_a is not a list of lists
    >>> matrix_mul([[3, 1, 2], [0, 2, 1], 4], [[0, 1, 1], [2, 0, 1], [1, 2, 0]])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list of lists

    # m_b is not a list of lists
    >>> matrix_mul([[3, 1, 2], [0, 2, 1], [1, 3, 2]], ['c', [2, 0, 1], [1, 2, 0]])
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list of lists

    # m_a is empty
    >>> matrix_mul([[]], [[0, 0, 0], [2, 0, 1], [1, 2, 0]])
    Traceback (most recent call last):
        ...
    ValueError: m_a can't be empty

    # m_b is empty
    >>> matrix_mul([[3, 1, 2], [0, 2, 1], [1, 3, 2]], [])
    Traceback (most recent call last):
        ...
    ValueError: m_b can't be empty

    # one element of m_a is not an int or float
    >>> matrix_mul([[1, 0, 2], [3, 5j, 2], [0, 2, 1]], [[2, 1, 2], [3, 0, 2], [1, 3, 2]])
    Traceback (most recent call last):
        ...
    TypeError: m_a should contain only integers or floats

    # one element of m_b is not an int or float
    >>> matrix_mul([[1, 0, 2], [3, 0, 2], [0, 2, 1]], [[2, 1, 2], [3, 0, 2], [1, 3, 's']])
    Traceback (most recent call last):
        ...
    TypeError: m_b should contain only integers or floats

    # m_a is not a rectangle
    >>> matrix_mul([[1, 0, 2], [3, 2, 2], [0, 1]], [[2, 1, 2], [3, 0, 2], [1, 3, 2]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_a must be of the same size

    # m_b is not a rectangle
    >>> matrix_mul([[1, 0, 2], [3, 2, 2], [0, 1, 1]], [[1, 2], [3, 0, 2], [1, 3, 2]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_b must be of the same size

    # m_a rows != m_b columns
    >>> matrix_mul([[1, 0], [3, 2, 2], [0, 1]], [[2, 1, 2], [3, 0, 2], [1, 3, 2]])
    Traceback (most recent call last):
        ...
    ValueError: m_a and m_b can't be multiplied

    """

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

    for xr in range(len(m_a)):
        for mbc in range(len(m_b[0])):
            for xc in range(len(m_b)):
                if not isinstance(m_a[xr], list):
                    raise TypeError("m_a must be a list of lists")
                if not isinstance(m_b[xc], list):
                    raise TypeError("m_b must be a list of lists")

                if not isinstance(m_a[xr][xc], (int, float)):
                    raise TypeError("m_a should contain "
                                    "only integers or floats")
                if not isinstance(m_b[xc][mbc], (int, float)):
                    raise TypeError("m_b should contain "
                                    "only integers or floats")
                if len(m_a[xr]) != len(m_a[0]):
                    raise TypeError("each row of m_a must be of the same size")
                if len(m_b[xc]) != len(m_b[0]):
                    raise TypeError("each row of m_b must be of the same size")
                cal += m_a[xr][xc] * m_b[xc][mbc]
            res.append(cal)
            cal = 0
        result.append(res)
        res = []
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)