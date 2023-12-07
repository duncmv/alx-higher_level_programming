#!/usr/bin/python3
"""Unittest for Square"""


import unittest
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):

    # Initialization tests
    def test_initialization_valid(self):
        squ1 = Square(10, 2, 3, 50)
        self.assertEqual(squ1.width, 10)
        self.assertEqual(squ1.height, 10)
        self.assertEqual(squ1.x, 2)
        self.assertEqual(squ1.y, 3)
        self.assertEqual(squ1.id, 50)

    def test_initialization_invalid(self):
        with self.assertRaises(TypeError):
            Square("10", 5)
        with self.assertRaises(ValueError):
            Square(-10, 5)

    # Property tests
    def test_width_setter_valid(self):
        squ = Square(10, 5)
        squ.width = 20
        self.assertEqual(squ.width, 20)

    def test_width_setter_invalid(self):
        squ = Square(10, 5)
        with self.assertRaises(TypeError):
            squ.width = "20"
        with self.assertRaises(TypeError):
            squ.width = True
        with self.assertRaises(TypeError):
            squ.width = {"ks": 0}
        with self.assertRaises(TypeError):
            squ.width = (0, 1)
        with self.assertRaises(TypeError):
            squ.width = []
        with self.assertRaises(ValueError):
            squ.width = -20
        with self.assertRaises(ValueError):
            squ.width = 0

    def test_height_setter_valid(self):
        squ = Square(10, 5)
        squ.height = 20
        self.assertEqual(squ.height, 20)

    def test_height_setter_invalid(self):
        squ = Square(10, 5)
        with self.assertRaises(TypeError):
            squ.height = "20"
        with self.assertRaises(TypeError):
            squ.height = True
        with self.assertRaises(TypeError):
            squ.height = {"ks": 0}
        with self.assertRaises(TypeError):
            squ.height = (0, 1)
        with self.assertRaises(TypeError):
            squ.height = []
        with self.assertRaises(ValueError):
            squ.height = -20
        with self.assertRaises(ValueError):
            squ.height = 0

    def test_x_setter_valid(self):
        squ = Square(10, 5)
        squ.x = 20
        self.assertEqual(squ.x, 20)

    def test_x_setter_invalid(self):
        squ = Square(10, 5)
        with self.assertRaises(TypeError):
            squ.x = "20"
        with self.assertRaises(TypeError):
            squ.x = True
        with self.assertRaises(TypeError):
            squ.x = {"ks"}
        with self.assertRaises(TypeError):
            squ.x = (0, 1)
        with self.assertRaises(TypeError):
            squ.x = []
        with self.assertRaises(ValueError):
            squ.x = -20

    def test_y_setter_valid(self):
        squ = Square(10, 5)
        squ.y = 20
        self.assertEqual(squ.y, 20)

    def test_y_setter_invalid(self):
        squ = Square(10, 5)
        with self.assertRaises(TypeError):
            squ.y = "20"
        with self.assertRaises(TypeError):
            squ.y = True
        with self.assertRaises(TypeError):
            squ.y = {"ks"}
        with self.assertRaises(TypeError):
            squ.y = (0, 1)
        with self.assertRaises(TypeError):
            squ.y = []
        with self.assertRaises(ValueError):
            squ.y = -20

    # Area method test
    def test_area(self):
        squ = Square(3)
        self.assertEqual(squ.area(), 9)

    # String representation test
    def test_str(self):
        squ = Square(2, 1, 1, 50)
        self.assertEqual(str(squ), "[Square] (50) 1/1 - 2")

    # Update method tests
    def test_update_args(self):
        squ = Square(1, 1, 1, 1)
        squ.update(10, 2, 3, 4)
        self.assertEqual(str(squ), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        squ = Square(1, 1, 1, 1)
        squ.update(size=9, y=8, x=7)
        self.assertEqual(str(squ), "[Square] (1) 7/8 - 9")

    def test_update_invalid(self):
        squ = Square(10, 10)
        with self.assertRaises(TypeError):
            squ.update(width="20")
        with self.assertRaises(ValueError):
            squ.update(height=-10)

    # Dictionary representation test
    def test_to_dictionary(self):
        squ = Square(3, 1, 2, 50)
        self.assertEqual(squ.to_dictionary(), {'id': 50, 'size': 3,
                                               'x': 1, 'y': 2})

    def test_display(self):
        squ = Square(2, 2, 2)
        expected_output = "\n\n" + ("  ##\n" * 2)

        capturedOutput = StringIO()         # Create StringIO object
        sys.stdout = capturedOutput         # and redisqu stdout.
        squ.display()                      # Call display method
        sys.stdout = sys.__stdout__         # Reset redisqu.

        self.assertEqual(capturedOutput.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
