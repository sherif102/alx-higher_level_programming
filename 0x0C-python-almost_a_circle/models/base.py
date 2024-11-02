#!/usr/bin/python3
"""
Module: base.py
Author: Shriff Abdulfatai
"""


class Base:
    """ defines the id of every object """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ generate dictionary repersentation of a list of dictionaries """
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return f"{json.dumps(list_dictionaries)}"

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json representation of list_objets to file """
        obj = cls.__name__
        filename = f"{obj}.json"

        if list_objs is None or list_objs == []:
            with open(filename, 'w') as file:
                file.write("[]")
            return

        with open(filename, 'w') as file:
            file.write('[')
            for x in list_objs:
                file.write(str(cls.to_json_string(x.to_dictionary())))
                if x is not list_objs[len(list_objs) - 1]:
                    file.write(", ")
            file.write(']')

    @staticmethod
    def from_json_string(json_string):
        """ loads json string to dictionary """
        if json_string is None or len(json_string) == 0:
            return []
        import json
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates an object instance from dictionary """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            result = []
            filename = f"{cls.__name__}.json"
            with open(filename, 'r') as file:
                readed = file.read()
                from_json = cls.from_json_string(readed)
                for x in from_json:
                    result.append(cls.create(**x))
            return result
        except FileNotFoundError:
            return []
