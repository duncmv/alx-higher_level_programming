#!/usr/bin/python3
"""This module defines a class Node of another class SinglyLinkedList
Node will contain data of type int and next_node of type Node
SinglyLinkedList will contain head and a method sorted_insert
"""


class Node:
    """This class defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (type(value) is Node or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly liked list with nodes from class Node
    """
    def __init__(self):
        self.__head = None

    def __repr__(self):
        temp = self.__head
        total = ""
        while temp:
            total += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                total += "\n"
        return total

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            x = self.__head
            prev = None
            while x and value > x.data:
                prev = x
                x = x.next_node
            if x is self.__head and prev is None:
                self.__head = Node(value, x)
            else:
                new = Node(value, x)
                prev.next_node = new
