#!/usr/bin/python3
"""Square class that inherits Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def area(self):
        return self._Rectangle__width ** 2