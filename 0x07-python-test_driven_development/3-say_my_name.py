#!/usr/bin/python3
"""
This mdule defines  function that prints a name
but checks first if they are strings
"""


def say_my_name(first_name, last_name=""):
    """ Prints a name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
