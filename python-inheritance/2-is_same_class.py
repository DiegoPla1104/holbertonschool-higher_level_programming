#!/usr/bin/python3
"""
    Module to check if obj is of the class
    passed
"""


def is_same_class(obj, a_class):
    """
        True if the object is exactly an instance
        of the specified class
        Otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
