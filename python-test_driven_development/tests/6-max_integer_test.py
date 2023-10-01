#!/usr/bin/python3
"""===============================
   6-max_integer_test.py Tests
   ===============================
"""

"""
   This is a test for the function 6-max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger is a class created specially for this case"""

    def test_max(self):
        """The function must retrieve the max integer from this test"""
        self.assertEqual(max_integer([1, 6, 10, 24, 758, 4, 3, 1]), 758)

    def test_max_iguales(self):
        """In this test they search in a list of the same value"""
        self.assertEqual(max_integer([6, 6, 6, 6, 6]), 6)

    def test_max(self):
        """In a list full of negative values"""
        self.assertEqual(max_integer([-1, -6, 10, -24, -758, 4, -3, 1]), 10)

    def test_max_none(self):
        """An empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_error(self):
        """Incorrect types of value of values"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'Mato'])