#!/usr/bin/python3
"""module reads a file and prints it"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
