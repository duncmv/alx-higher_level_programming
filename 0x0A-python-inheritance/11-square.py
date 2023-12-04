#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square class that inherits Rectangle"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
