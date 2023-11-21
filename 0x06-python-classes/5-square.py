#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
Size defaults to 0. Raise errors on invalid inputs.
"""


class Square:
    """A class that defines a square by size"""
    def __init__(self, size=0):
        self.size = size

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
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
