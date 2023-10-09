#!/usr/bin/python3
import unittest
Base = __import__(models/base.py).Base
Rectangle = __import__(models/rectangle.py).Rectangle
"""
    Test for rectangle.py
"""


class TestBase(unittest.TestCase):
    def ValueErrorWidth(Rectangle):
        