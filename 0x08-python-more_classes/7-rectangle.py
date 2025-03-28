#!/usr/bin/python3
"""
Module: 2-rectangle.py
Author: Sheriff Abdulfatai
"""


class Rectangle():
    """ defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ prints the string class format """
        string = []
        if self.__width == 0 or self.__height == 0:
            return ''
        for x in range(self.__height):
            string.append(str(self.print_symbol) * self.__width)
            if x < self.__height - 1:
                string.append('\n')
        return ''.join(string)

    def __repr__(self):
        x = ["Rectangle", '(', str(self.__width),
             ', ', str(self.__height), ')']
        return ''.join(x)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
