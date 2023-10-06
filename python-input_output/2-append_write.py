#!/usr/bin/python3
"""
    Task 1
"""


def append_write(filename="", text=""):
    """
        Function to write on a .txt file
    """
    with open(filename, "a", encoding="utf=8") as f:
        c = f.write(text)
    return c
