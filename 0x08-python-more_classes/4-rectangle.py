#!/usr/bin/python3
"""definition of Rectangle class
"""


class Rectangle:
    """class Rectangle
    with width and height
    methods to calculate area and perimeter
    as well as __str__ and __repr__ methods
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        new = ""
        for i in range(self.__height):
            new += ('#' * self.__width)
            if i != self.__height - 1:
                new += '\n'
        return new

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
