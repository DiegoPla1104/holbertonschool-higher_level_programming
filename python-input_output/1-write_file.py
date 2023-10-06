#!/usr/bin/python3
"""
    Task 1
"""


def write_file(filename="", text=""):
    """
        Function to write on a .txt file
    """
    with open(filename, "w", encoding="utf=8") as f:
        c = f.write(text)
    return c
