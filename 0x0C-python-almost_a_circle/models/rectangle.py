#!/usr/bin/python3
"""
Module: base.py
Author: Shriff Abdulfatai
"""


from base import Base
class Rectangle(Base):
    """ rectangle class inheriting from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization with super id"""
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ get width """
        return self.__width
    @width.setter
    def width(self, value):
        """ set width value """
        self.__width = value

    @property
    def height(self):
        """ get width """
        return self.__height
    @height.setter
    def height(self, value):
        """ set width value """
        self.__height = value

    @property
    def x(self):
        """ get width """
        return self.__x
    @x.setter
    def x(self, value):
        """ set width value """
        self.__x = value

    @property
    def y(self):
        """ get width """
        return self.__y
    @x.setter
    def y(self, value):
        """ set width value """
        self.__y = value
