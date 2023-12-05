#!/usr/bin/python3
"""module writes to a file"""


def write_file(filename="", text=""):
    """writes a file"""
    with open(filename, "w", encoding="UTF-8") as f:
        chars = f.write(text)
        return chars
