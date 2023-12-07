#!/usr/bin/python3
"""defines Base class"""


import json
import os.path


class Base:
    """ will be the base class of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of  to a file"""
        if list_objs is None:
            list_objs = []
        json_string = Base.to_json_string([i.to_dictionary()
                                           for i in list_objs])

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        insts = []
        if os.path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
                lis = Base.from_json_string(f.read())
                for i in lis:
                    insts.append(cls.create(**i))
        return insts

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
            for i in list_objs:
                csv_str = f"{i.id},"
                if cls.__name__ == "Rectangle":
                    csv_str += f"{i.width},{i.height},"
                elif cls.__name__ == "Square":
                    csv_str += f"{i.size},"
                csv_str += f"{i.x},{i.y}\n"
                f.write(csv_str)

    @classmethod
    def load_from_file_csv(cls):
        insts = []
        if os.path.isfile(f"{cls.__name__}.csv"):
            with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as f:
                for line in f:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, list(line.split(",")))
                        insts.append(cls(width, height, x, y, id))
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, list(line.split(",")))
                        insts.append(cls(size, x, y, id))
        return insts
