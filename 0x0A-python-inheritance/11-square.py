#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square class that inherits Rectangle"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """returns the area"""
        return self.__size ** 2
    
    def __str__(self):
        return "[Square] {}/{}".format(self.__size,
                                       self.__size)
