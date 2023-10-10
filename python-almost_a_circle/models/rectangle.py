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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    print_symbol = "#"

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

    def area(self):
        """Calculates the area of the rectangle"""

        return (self.__height * self.__width)

    def display(self):
        """Displays the Rectangle"""
        saved_str = ""
        if self.__height == 0 or self.__width == 0:
            return ('')
        for i in range(self.__height):
            saved_str += str(f"{self.print_symbol}" * self.__width) + '\n'
        saved_str = saved_str[:-1]
        return saved_str
