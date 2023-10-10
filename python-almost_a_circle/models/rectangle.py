#!/usr/bin/python3
"""
    Module
"""
from models.base import Base


class Rectangle(Base):
    """
        Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defining width cualifications"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defining height cualifications"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Defining x cualifications"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Defining y cualifications"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
