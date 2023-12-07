#!/usr/bin/python3
"""unittest for Base class"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_auto_assignment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_id_manual_assignment(self):
        base3 = Base(12)
        self.assertEqual(base3.id, 12)

    def test_json_serialization(self):
        dict_list = [{"id": 12}, {"id": 13}]
        json_string = Base.to_json_string(dict_list)
        self.assertIsInstance(json_string, str)

    def test_json_deserialization(self):
        json_string = '[{"id": 12}, {"id": 13}]'
        objects = Base.from_json_string(json_string)
        self.assertEqual(len(objects), 2)
        self.assertDictEqual(objects[0], {"id": 12})

    def test_save_to_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([rect1, rect2])
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_load_from_file(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([rect1, rect2])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 2)
        self.assertIsInstance(rects[0], Rectangle)
        self.assertIsInstance(rects[1], Rectangle)

    def test_save_to_file_with_square(self):
        square1 = Square(5, 1, 2, 1)
        square2 = Square(7, 2, 3, 2)
        Square.save_to_file([square1, square2])
        self.assertTrue(os.path.isfile('Square.json'))

    def test_load_from_file_with_square(self):
        square1 = Square(5, 1, 2, 1)
        square2 = Square(7, 2, 3, 2)
        Square.save_to_file([square1, square2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)


if __name__ == '__main__':
    unittest.main()
