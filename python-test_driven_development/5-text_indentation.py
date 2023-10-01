#!/usr/bin/python3
"""
    This function splits a given text by ". , ? :"
    It takes those characters and puts a new line after them
"""


def text_indentation(text):
    """
        As said previously, it splits the given text.
        But first it checks if it's a string.
        It gives an error message if it isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tx1 = text.replace('.', '.\n\n').replace('?', '?\n\n')\
        .replace(':', ':\n\n')
    tx = tx1.strip(" ")
    print("{:s}".format(tx))
