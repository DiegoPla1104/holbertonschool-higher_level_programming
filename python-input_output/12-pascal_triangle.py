#!/usr/bin/python3
"""
    Pascale triangle
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers
        representing the Pascals triangle of n
    """

    if n <= 0:
        return []

    t = []
    for row in range(n):
        t.append([1])

        for a in range(1, row):
            t[row].append(t[row - 1][a - 1] + t[row - 1][a])

        if row is not 0:
            t[row].append(1)
    return t
