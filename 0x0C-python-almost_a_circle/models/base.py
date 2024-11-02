#!/usr/bin/python3
"""
Module: base.py
Author: Shriff Abdulfatai
"""


import json
import csv


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
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ generate a csv file """
        filename = f"{cls.__name__}.csv"
        if not list_objs:
            return
        with open(filename, 'w', newline='') as file:
            if cls.__name__ == 'Rectangle':
                field = ['id', 'width', 'height', 'x', 'y']
            else:
                field = ['id', 'size', 'x', 'y']

            csvwriter = csv.DictWriter(file, fieldnames=field)
            csvwriter.writeheader()
            for x in list_objs:
                csvwriter.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ loads csv file to instance """
        filename = f"{cls.__name__}.csv"
        result = []
        field = ['id', 'width', 'height', 'x', 'y', 'size']
        try:
            with open(filename, newline='') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    for key in row:
                        if key in field:
                            row[key] = int(row[key])
                    result.append(cls.create(**row))
            return result
        except FileNotFoundError:
            return []
