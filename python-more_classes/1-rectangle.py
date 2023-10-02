#!/usr/bin/python3
"""
    Defining an object class named Square
"""


class Rectangle:
    """
        Creating the attribute for sai object
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Property setter for square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defining height cualifications"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Property setter for square"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defining size cualifications"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
