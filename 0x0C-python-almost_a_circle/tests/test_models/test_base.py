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

    def test_save_to_file_csv_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        self.assertTrue(os.path.isfile('Rectangle.csv'))

        with open('Rectangle.csv', 'r') as file:
            content = file.read().strip().split("\n")
            self.assertEqual(content[0], "1,10,7,2,8")
            self.assertEqual(content[1], "2,2,4,0,0")

    def test_save_to_file_csv_square(self):
        square1 = Square(5, 1, 2, 1)
        square2 = Square(7, 2, 3, 2)
        Square.save_to_file_csv([square1, square2])
        self.assertTrue(os.path.isfile('Square.csv'))

        with open('Square.csv', 'r') as file:
            content = file.read().strip().split("\n")
            self.assertEqual(content[0], "1,5,1,2")
            self.assertEqual(content[1], "2,7,2,3")

    def test_load_from_file_csv_rectangle(self):
        Rectangle.save_to_file_csv([Rectangle(10, 7, 2, 8, 1),
                                    Rectangle(2, 4, 0, 0, 2)])
        rects = Rectangle.load_from_file_csv()
        self.assertEqual(len(rects), 2)
        self.assertIsInstance(rects[0], Rectangle)
        self.assertEqual(rects[0].width, 10)
        self.assertEqual(rects[0].height, 7)

    def test_load_from_file_csv_square(self):
        Square.save_to_file_csv([Square(5, 1, 2, 1), Square(7, 2, 3, 2)])
        squares = Square.load_from_file_csv()
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 5)

    @classmethod
    def tearDownClass(cls):
        """Cleanup files created during tests"""
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
