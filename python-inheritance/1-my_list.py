#!/usr/bin/python3
"""
    Module to print a sorted list
"""


class MyList(list):
    """
        Class named MyList
    """

    def print_sorted(self):
        """
            Prints the list but sorted (ascending sort)
        """
        print(sorted(self))
