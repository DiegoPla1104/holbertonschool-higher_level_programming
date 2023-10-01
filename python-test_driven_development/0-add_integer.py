#!/usr/bin/python3
"""
    This Module is used to add two numbers


"""


def add_integer(a, b=98):
    """
        The two variables that are passed to this function are a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
