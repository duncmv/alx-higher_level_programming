#!/usr/bin/python3
"""this module defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """return True if obj is an instance of specified class
    or if the object is an instance of a class that inherited
    """
    return isinstance(obj, a_class)
