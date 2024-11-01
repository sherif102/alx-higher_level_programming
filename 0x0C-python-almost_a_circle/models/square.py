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
        self.__size = size

    @property
    def size(self):
        """ get the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets value for size """
        self.__size = value
        setattr(self, "width", self.__size)
        setattr(self, "height", self.__size)

    def __str__(self):
        """ define a customized print string """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"
