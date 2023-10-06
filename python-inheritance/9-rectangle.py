#!/usr/bin/python3
"""
    Module:
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class BaseGeometry"""


class Rectangle(BaseGeometry):
    """
        Class Rectangle
    """
    def __init__(self, width, height):
        """
            init
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
            Area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
            Self str
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
