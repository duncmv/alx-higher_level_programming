#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 5, 3, 7, 2]), 7)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -5, -3, -7, -2]), -1)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([-1, 5, -3, 7, -2]), 7)

        # Test with a list containing only one integer
        self.assertEqual(max_integer([42]), 42)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

    def test_max_integer_empty_list(self):
        # Test with an empty list (should return None)
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
