#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak"""
    list_of_integers.sort()
    try:
        return list_of_integers[-1]
    except IndexError:
        return None
