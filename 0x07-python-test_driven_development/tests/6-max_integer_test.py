#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertAlmostEqual(max_integer([3, 2, 0]), 3)

    def test_list_str(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "a"])

    def test_max_int_end(self):
        self.assertAlmostEqual(max_integer([1, 4, 8]), 8)

    def test_max_int_middle(self):
        self.assertAlmostEqual(max_integer([1, 10, 2]), 10)

    def test_int_negative(self):
        self.assertAlmostEqual(max_integer([1, -10, 2]), 2)

    def test_int_all_negative(self):
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)

    def test_list_empty(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_list_one_element(self):
        self.assertAlmostEqual(max_integer([1]), 1)
