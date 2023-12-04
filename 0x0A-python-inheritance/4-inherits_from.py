#!/usr/bin/python3
"""defines a function inherits_from"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly)the specified class
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
