#!/usr/bin/python3
"""class MyInt that inherits int"""


class MyInt(int):
    """class MyInt"""
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
