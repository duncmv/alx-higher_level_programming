#!/usr/bin/python3
"""module reads a file and prints it"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read())
