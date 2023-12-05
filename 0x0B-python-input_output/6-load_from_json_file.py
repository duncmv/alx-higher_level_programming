#!/usr/bin/python3
"""module defines load_from_json_file function"""


import json


def load_from_json_file(my_obj, filename):
    """ creates an Object from a “JSON file"""
    with open(filename, encoding="utf-8") as f:
        json.load(my_obj, f)
