#!/usr/bin/python3
"""max integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class MyTestCase(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_max(self):
        self.assertEqual(max_integer([8, 3, 9, 7]), 9)
        self.assertEqual(max_integer([56]), 56)
        self.assertEqual(max_integer([5, -8, 10]), 10)
        self.assertEqual(max_integer([5.67, 5.66, 5.65]), 5.67)
        self.assertEqual(max_integer([2, 5, 9, 87, 215, 8, 32]), 215)
        self.assertEqual(max_integer([584579621, 584579622]),  584579622)
        self.assertEqual(max_integer([10, -8, 10, 5, 3]), 10)
        self.assertEqual(max_integer([-10, -8, -5, -3]), -3)


    def test_value(self):
        self.assertRaises(TypeError, max_integer(), [5, "hi", 0])
