#!/usr/bin/python3
"""
Module: 6-max_integer_test
Author: Sheriff Abdulfatai

Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests the funtion max_integer """

    def test_max_integer(self):
        self.assertEqual(max_integer([7, 8, 2]), 8)
        self.assertEqual(max_integer([7, 8, 20]), 20)
        self.assertEqual(max_integer([17, 8, 2]), 17)
        self.assertEqual(max_integer(['a', 'y', 't']), 'y')
        self.assertEqual(max_integer([2]), 2)
        with self.assertRaises(TypeError):
            max_integer([7, 8, '2'])
        with self.assertRaises(TypeError):
            max_integer(6)
        self.assertEqual(max_integer(), None)
        with self.assertRaises(TypeError):
            max_integer(6, 2)
