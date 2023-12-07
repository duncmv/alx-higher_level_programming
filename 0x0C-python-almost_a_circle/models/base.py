#!/usr/bin/python3
"""defines Base class"""


import json
import os.path
import turtle


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
        """saves objects in csv"""
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
        """loads objects from csv"""
        insts = []
        if os.path.isfile(f"{cls.__name__}.csv"):
            with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as f:
                for line in f:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, list(line.split(
                            ",")))
                        insts.append(cls(width, height, x, y, id))
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, list(line.split(",")))
                        insts.append(cls(size, x, y, id))
        return insts

    @staticmethod
    def draw_axes(pen):
        """Draw X and Y axes and mark them every 20 pixels"""
        pen.up()
        pen.goto(-200, 0)
        pen.down()
        pen.goto(200, 0)
        pen.up()
        pen.goto(0, -200)
        pen.down()
        pen.goto(0, 200)
        pen.up()
        for i in range(-180, 201, 20):
            if i != 0:
                pen.goto(i, -3)
                pen.down()
                pen.goto(i, 3)
                pen.up()

                pen.goto(-3, i)
                pen.down()
                pen.goto(3, i)
                pen.up()

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the objects
        - takes size, width, height as number of pixels
        - takes x and y as coordinates relative to origin(0,0)
        - prints objects in different colors
        with its top-left vertex at the (x,y) coordinate
        - The axes are marked every 20 pixels for verification
        """

        window = turtle.Screen()
        window.title("Rectangle and Square Drawing")

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed('fastest')

        Base.draw_axes(pen)

        pen.speed('normal')
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        color_index = 0
        for rect in list_rectangles:
            pen.color(colors[color_index % len(colors)])
            Base.draw_shape(pen, rect.x, rect.y, rect.width, rect.height)
            color_index += 1

        for square in list_squares:
            pen.color(colors[color_index % len(colors)])
            Base.draw_shape(pen, square.x, square.y, square.size, square.size)
            color_index += 1

        turtle.done()

    @staticmethod
    def draw_shape(pen, x, y, width, height):
        """helper function for draw"""
        pen.up()
        pen.goto(0, 0)
        pen.goto(x, y)
        pen.down()
        for _ in range(2):
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)
