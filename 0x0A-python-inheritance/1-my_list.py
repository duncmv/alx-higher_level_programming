#!/usr/bin/python3
"""class MyList that inherits list and has a public method
"""


class MyList(list):
    """class that inherits list and has a print sorted method"""
    def print_sorted(self):
        """prints the list but sorted in ascending order"""
        print(sorted(self))
