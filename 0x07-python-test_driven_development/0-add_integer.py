#!/usr/bin/python3
"""This module defines a function that adds two integers
"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats  as integer
    Else, raises TypeError
    """
    check = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(check):
        return int(a) + int(b)

    for x, y in list(zip(check, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
