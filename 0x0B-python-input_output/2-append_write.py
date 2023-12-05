#!/usr/bin/python3
"""module appends to a file"""


def append_write(filename="", text=""):
    """writes a file"""
    with open(filename, "a", encoding="utf-8") as f:
        chars = f.write(text)
        return chars
