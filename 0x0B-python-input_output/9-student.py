#!/usr/bin/python3
"""
Module: 9-student.py.py
Author: Sheriff Abdulfatai
"""


class Student():
    """ defines a student class s"""
    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ generate dictionary representation of the class """
        result = {}
        for x in self.__dict__:
            result[x] = self.__dict__[x]
        return result
