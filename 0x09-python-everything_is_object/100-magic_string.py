#!/usr/bin/python3
def magic_string():
    magic_string.i = 1 if not hasattr(magic_string, 'i') else magic_string.i+1
    return ("BestSchool, " * (magic_string.i - 1)) + "BestSchool"
