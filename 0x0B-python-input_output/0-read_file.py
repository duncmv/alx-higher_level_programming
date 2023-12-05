#!/usr/bin/python3
"""module reads a file and prints it"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
