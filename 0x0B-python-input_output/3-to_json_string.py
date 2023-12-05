#!/usr/bin/python3
"""module defines to_json_string function"""


import json


def to_json_string(my_obj):
    """returns the json string of an object"""
    return json.dumps(my_obj)
