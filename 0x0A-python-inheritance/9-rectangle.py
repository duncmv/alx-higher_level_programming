#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""rectangle class that inherits BaseGeometry"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
