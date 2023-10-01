#!/usr/bin/python3
"""
    This function is the same as the last proyect
"""


def print_square(size):
    """
        It prints a square if size is a positive int
        Otherwise it pops an error messege dependig
        if size is less than 0 or isn't an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for a in range(size):
        print("#" * size)
