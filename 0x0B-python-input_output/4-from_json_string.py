#!/usr/bin/python3
"""module defines from_json_string function"""


import json


def from_json_string(my_str):
    """returns the obect represente by json string"""
    return json.dumps(my_str)
