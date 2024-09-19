#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for s in my_string:
        if s == 'c' or s == 'C':
            continue
        new_string.append(s)
    return ''.join(new_string)
