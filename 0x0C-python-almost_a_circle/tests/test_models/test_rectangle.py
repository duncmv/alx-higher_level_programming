#!/usr/bin/python3
"""Unittest for rectangle"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """test class for rectangle"""

    # Initialization tests
    def test_initialization_valid(self):
        rect1 = Rectangle(10, 5, 2, 3, 50)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 2)
        self.assertEqual(rect1.y, 3)
        self.assertEqual(rect1.id, 50)

    def test_initialization_invalid(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

    # Property tests
    def test_width_setter_valid(self):
        rect = Rectangle(10, 5)
        rect.width = 20
        self.assertEqual(rect.width, 20)

    def test_width_setter_invalid(self):
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.width = "20"
        with self.assertRaises(TypeError):
            rect.width = True
        with self.assertRaises(TypeError):
            rect.width = {"ks": 0}
        with self.assertRaises(TypeError):
            rect.width = (0, 1)
        with self.assertRaises(TypeError):
            rect.width = []
        with self.assertRaises(ValueError):
            rect.width = -20
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_setter_valid(self):
        rect = Rectangle(10, 5)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_height_setter_invalid(self):
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.height = "20"
        with self.assertRaises(TypeError):
            rect.height = True
        with self.assertRaises(TypeError):
            rect.height = {"ks": 0}
        with self.assertRaises(TypeError):
            rect.height = (0, 1)
        with self.assertRaises(TypeError):
            rect.height = []
        with self.assertRaises(ValueError):
            rect.height = -20
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_setter_valid(self):
        rect = Rectangle(10, 5)
        rect.x = 20
        self.assertEqual(rect.x, 20)

    def test_x_setter_invalid(self):
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.x = "20"
        with self.assertRaises(TypeError):
            rect.x = True
        with self.assertRaises(TypeError):
            rect.x = {"ks"}
        with self.assertRaises(TypeError):
            rect.x = (0, 1)
        with self.assertRaises(TypeError):
            rect.x = []
        with self.assertRaises(ValueError):
            rect.x = -20

    def test_y_setter_valid(self):
        rect = Rectangle(10, 5)
        rect.y = 20
        self.assertEqual(rect.y, 20)

    def test_y_setter_invalid(self):
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.y = "20"
        with self.assertRaises(TypeError):
            rect.y = True
        with self.assertRaises(TypeError):
            rect.y = {"ks"}
        with self.assertRaises(TypeError):
            rect.y = (0, 1)
        with self.assertRaises(TypeError):
            rect.y = []
        with self.assertRaises(ValueError):
            rect.y = -20

    # Area method test
    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    # String representation test
    def test_str(self):
        rect = Rectangle(3, 2, 1, 1, 50)
        self.assertEqual(str(rect), "[Rectangle] (50) 1/1 - 3/2")

    # Update method tests
    def test_update_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(10, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (10) 4/5 - 2/3")

    def test_update_kwargs(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(height=10, width=9, y=8, x=7)
        self.assertEqual(str(rect), "[Rectangle] (1) 7/8 - 9/10")

    def test_update_invalid(self):
        rect = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            rect.update(width="20")
        with self.assertRaises(ValueError):
            rect.update(height=-10)

    # Dictionary representation test
    def test_to_dictionary(self):
        rect = Rectangle(3, 4, 1, 2, 50)
        self.assertEqual(rect.to_dictionary(), {'id': 50, 'width': 3,
                                                'height': 4, 'x': 1, 'y': 2})

    def test_display(self):
        rect = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n" + ("  ##\n" * 3)

        capturedOutput = StringIO()         # Create StringIO object
        sys.stdout = capturedOutput         # and redirect stdout.
        rect.display()                      # Call display method
        sys.stdout = sys.__stdout__         # Reset redirect.

        self.assertEqual(capturedOutput.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
