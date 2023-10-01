#!/usr/bin/python3
"""
    This module divies the ints inide a matrix
    by a specified number
"""


def matrix_divided(matrix, div):
    """
        This is said function.
        It cheacks that the matrix holds only integers
        If not raises a type error
        Then checks the div if its an int or a float and if it's 0
        Afterwards checks if the rows have the same length
        And finally creates a new list and appends the result of the division
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
            integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    l0 = []
    for a in matrix:
        if type(a) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")

        if len(a) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        l1 = []
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")

            l1.append(round(b / div, 2))
        l0.append(l1)
    return l0
