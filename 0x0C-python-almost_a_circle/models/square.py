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

    def __str__(self):
        """ define a customized print string """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"
