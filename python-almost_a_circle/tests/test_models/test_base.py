#!/usr/bin/python3
import unittest
Base = __import__(models/base.py).Base
"""
    Tests for the file named base.py
"""


class TestBase(unittest.TestCase):
    def TestId(self):
        self.assertEqual(id, None)

    def TestIdNum(self):
        self.assertEqual(id, 12312)
