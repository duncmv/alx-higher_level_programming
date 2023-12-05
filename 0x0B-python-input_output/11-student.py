#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """
    Attributes:
        first_name
        last_name
        age
    to_json method that retrieves a dict rep of instance"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        toggle = 0
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    toggle = 1
                    break
            if toggle == 0:
                atts = vars(self)
                att_filtered = {k: atts[k] for k in attrs if k in atts}
                return att_filtered
        return vars(self)

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
