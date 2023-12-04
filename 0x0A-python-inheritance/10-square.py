#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square class that inherits Rectangle"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def area(self):
        return self._Rectangle__width ** 2