#!/usr/bin/python3
""" This module defines a -node- and a -singly linked list-
with all the required attributes """


class Node:
    """ the creation of a new node """
    def __init__(self, data, next_node=None):
        """ initializes the data and new_node attribute """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

        # if ((next_node is not None) or (next_node is not Node)):
        #     raise TypeError("next_node must be a Node object")
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
        if ((value is not None) or (value is not Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """
    def __init__(self):
        """ initializes the head """
        self.__head = []

    def __repr__(self):
        """ format the class to be printable """
        for i in self.__head:
            print("{}".format(i.data))
    
    def sorted_insert(self, value):
        """ insert new node in a sorted manner """
        x = Node(value)
        self.__head.append(x)
