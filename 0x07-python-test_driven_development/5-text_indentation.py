#!/usr/bin/python3
"""
Module: 4-print_square
Author: Sheriff Abdulfatai
"""


def text_indentation(text):
    """
    Prints text with a custom formating.
    Two blank lines after every '.' :' and '?'

    >>> text_indentation("where are you coming from")
    where are you coming from

    >>> text_indentation("can you come over? if yes, good")
    can you come over?
    <BLANKLINE>
    <BLANKLINE>
    if yes, good

    >>> text_indentation("here. we: go? smile")
    here.
    <BLANKLINE>
    <BLANKLINE>
    we:
    <BLANKLINE>
    <BLANKLINE>
    go?
    <BLANKLINE>
    <BLANKLINE>
    smile

    >>> text_indentation(2)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    custom = ['.', ':', '?']
    last = ''
    if text[0] == ' ':
        last = '.'

    for x in range(len(text)):
        if text[x] == ' ' and last in custom:
            continue

        if text[x] in custom:
            last = text[x]
            print(text[x], end='')
            print('\n' * 2)
        else:
            print(text[x], end='')
            last = text[x]
