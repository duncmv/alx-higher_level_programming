#!/usr/bin/python3
from sys import stderr as e


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as x:
        print("Exception: {}".format(x), file=e)
        return False
