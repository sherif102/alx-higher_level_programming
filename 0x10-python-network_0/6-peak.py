#!/usr/bin/python3
"""
Module: 6-peak.py
Author: Sheriff Abdulfatai
"""


def find_peak(list_of_integers):
    """finds the peak in a list"""
    # linear search solution with Big O of O(n)
    """
    list_len = len(list_of_integers) - 1
    start = 1
    if list_len < 0:
        return None
    if list_len < 3 and list_len > 0:
        return sorted(list_of_integers)[list_len]
    while start < list_len and list_len > 1:
        peak = start
        if list_of_integers[peak] > list_of_integers[peak - 1] and\
                list_of_integers[peak] > list_of_integers[peak + 1]:
            return list_of_integers[peak]
        start += 1
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[list_len] > list_of_integers[-2]:
        return list_of_integers[list_len]
    """

    # binary search solution with Big O of O(log(n))
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
