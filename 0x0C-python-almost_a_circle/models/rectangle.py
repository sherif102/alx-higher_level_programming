#!/usr/bin/python3
"""
Module: base.py
Author: Shriff Abdulfatai
"""


from models.base import Base


class Rectangle(Base):
    """ rectangle class inheriting from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization with super id"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if int(x) < 0:
            raise ValueError("x must be >= 0")
        if int(y) < 0:
            raise ValueError("y must be >= 0")
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get width """
        return self.__height

    @height.setter
    def height(self, value):
        """ set width value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get width """
        return self.__x

    @x.setter
    def x(self, value):
        """ set width value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if int(value) < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get width """
        return self.__y

    @y.setter
    def y(self, value):
        """ set width value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if int(value) < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ define the area """
        return self.__width * self.__height

    def display(self):
        """ prints the display representation """
        for x in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ define the string representation """
        return str(f"[Rectangle] ({Rectangle.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
