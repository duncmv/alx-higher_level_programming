#!/usr/bin/python3
"""this module defines the is_same_class function"""


def is_same_class(obj, a_class):
    """return True if obj is exactly an instance of specified class"""
    return type(obj) == a_class
