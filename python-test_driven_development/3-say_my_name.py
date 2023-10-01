#!/usr/bin/python3
"""
    This module prints the inputed First and Last name
"""


def say_my_name(first_name, last_name=""):
    """
        Say my name (Aside from being a reference to Breaking Bad)
        Takes an input in the form of two strings (first_name and last_name)
        Checks if they are strings
        And prints them in the order "first_name" and "last_name"
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
