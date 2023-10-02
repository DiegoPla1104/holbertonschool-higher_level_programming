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
        """Defining width cualifications"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Property setter for square"""
        return self.__height * self.__width

    def perimeter(self):
        """Defining perimeter cualifications"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        saved_str = ""
        if self.__height == 0 or self.__width == 0:
            return ('')
        for i in range(self.__height):
            saved_str += str("#" * self.__width) + '\n'
        saved_str = saved_str[:-1]
        return saved_str
