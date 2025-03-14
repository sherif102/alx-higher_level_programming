#!/usr/bin/python3
"""
Module: square.py
Author: Shriff Abdulfatai
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines the square object """
    def __init__(self, size, x=0, y=0, id=None):
        """ square initialization """
        super().__init__(size, size, x, y, id)
        self.__x = x
        self.__y = y
        self.__width = size

    @property
    def size(self):
        """ get the size """
        return self.__width

    @size.setter
    def size(self, value):
        """ sets value for size """
        self.__width = value
        setattr(self, "width", value)
        setattr(self, "height", value)

    def __str__(self):
        """ define a customized print string """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    def update(self, *args, **kwargs):
        """ update the current values """
        att = ['id', 'size', 'x', 'y']
        for x, y in zip(att, args):
            setattr(self, x, y)
        for key, values in kwargs.items():
            setattr(self, key, values)

    def to_dictionary(self):
        """ generates dictionary representation """
        result = {}
        values = ['id', 'size', 'x', 'y']
        for x in values:
            result[x] = getattr(self, x)
        return result
