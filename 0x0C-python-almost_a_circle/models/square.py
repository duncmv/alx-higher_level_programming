#!/usr/bin/python3
"""defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Base
    It has three public methods:
        area - returns the area
        display - prints the square using #
        update - updates attributes using args or kwargs
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        atts = ('id', 'size', 'x', 'y')
        for attr, value in zip(atts, args):
            setattr(self, attr, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic
