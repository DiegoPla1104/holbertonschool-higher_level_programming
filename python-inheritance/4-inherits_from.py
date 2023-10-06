#!/usr/bin/python3
"""
    Module to check if obj is an instance of a class inherited by a_class
"""


def inherits_from(obj, a_class):
    """
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
        Otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True

    else:
        return False
