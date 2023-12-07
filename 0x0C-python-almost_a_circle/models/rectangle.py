#!/usr/bin/python3
"""defines a Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    It has three public methods:
        area - returns the area
        display - prints the rectangle using #
        update - updates attributes using args or kwargs
    """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        return f"""[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"""

    def update(self, *args, **kwargs):
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        atts = ('id', 'width', 'height', 'x', 'y')
        for attr, value in zip(atts, args):
            setattr(self, attr, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {'id': self.id, 'width': self.__width,
               'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dic
