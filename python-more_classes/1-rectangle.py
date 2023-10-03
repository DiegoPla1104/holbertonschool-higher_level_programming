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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def height(self):
        """Property setter for square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defining height cualifications"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Property setter for square"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defining size cualifications"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
