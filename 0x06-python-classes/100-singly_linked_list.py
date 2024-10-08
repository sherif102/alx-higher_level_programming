#!/usr/bin/python3
""" This module defines a -node- and a -singly linked list-
with all the required attributes """


class Node:
    """ the creation of a new node """
    def __init__(self, data, next_node=None):
        """ initializes the data and new_node attribute """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

        if (not isinstance(next_node, Node)) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieving of data """
        return self.__data

    @data.setter
    def data(self, value):
        """ set new value for data """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ retrieving of next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setting value for next_node """
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """
    def __init__(self):
        """ initializes the head """
        self.__head = []

    def __repr__(self):
        """ format the class to be printable """
    
    def sorted_insert(self, value):
        """ insert new node in a sorted manner """

