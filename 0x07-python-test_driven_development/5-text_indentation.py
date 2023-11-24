#!/usr/bin/python3
"""this module defines afunction that indents a string whenever it
encounters . ? or :
"""


def text_indentation(text):
    """indent func"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    new = ""
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in ['.', '?', ':']:
            continue
        new += text[i]
        if text[i] in ['.', '?', ':']:
            new += "\n\n"

    print(new, end="")
