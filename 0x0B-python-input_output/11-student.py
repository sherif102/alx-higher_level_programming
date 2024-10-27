#!/usr/bin/python3
"""
Module: 11-student.py.py
Author: Sheriff Abdulfatai
"""


class Student():
    """ defines a student class s"""
    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, arg=['.']):
        """ generate dictionary representation of the class """
        result = {}
        if len(arg) > 0 and arg[0] != '.':
            for i in arg:
                if hasattr(self, i):
                    result[i] = self.__dict__[i]
            return result
        elif len(arg) == 0:
            return {}
        else:
            for x in self.__dict__:
                result[x] = self.__dict__[x]
            return result

    def reload_from_json(self, json):
        """ replaces attributes of the object """
        if len(json) == 0:
            return
        self.__dict__ = json
