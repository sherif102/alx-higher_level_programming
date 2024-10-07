#!/usr/bin/python3
""" This module defines a class -Square- with
the neccessary attributes """


class Square:
    """ a class with  private attribute -size-
     and public method -area- """
    def __init__(self, size=0, position=(0, 0)):
        """ validation of size and position value,
        if it is less than 0 a value eror is
        raised and must be an integer """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position[0]) and type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((len(position) != 2) or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ returns the square area """
        return (self.__size ** 2)

    @property
    def size(self):
        """ retrieve the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets value for size attribute """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrieves the value of position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets new value for the position """
        if (type(value[0]) and type(value[1]) is not int):
            raise TypeError("value must be a tuple of 2 positive integers")
        elif ((len(value) != 2) or value[0] < 0 or value[1] < 0):
            raise TypeError("value must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints -#- in square """
        if (self.__size == 0):
            print()
        else:
            if self.__position[1] != 0:
                print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
