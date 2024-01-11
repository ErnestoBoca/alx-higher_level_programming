#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Tests the max_integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -1]), 3)
        self.assertEqual(max_integer([10, 2, 3, -1]), 10)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-2, -1, -6, -10]), -1)
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([], 2)
