#!/usr/bin/python3
"""
    Task 0
"""


def read_file(filename=""):
    """
        Function to print a .txt file
    """
    with open(filename, "r", encoding="utf=8") as f:
        text = f.read()
        print(text)
