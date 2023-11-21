#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size and position.
Size defaults to 0. Position defalts to (0, 0) Raise errors on invalid inputs.
"""


class Square:
    """A class that defines a square by size and position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self. position = position

    @property
    def size(self):
        """ This is a getter method for size

        The setter method checks for Type and value errors"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """ This is a getter method for position

        The setter method checks for Type and values for errors"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        function that returns area

        Returns:
            the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        function that prints square with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
