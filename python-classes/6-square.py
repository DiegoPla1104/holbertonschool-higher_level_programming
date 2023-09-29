#!/usr/bin/python3
"""
    Defining an object class named Square
"""


class Square:
    """
        Creating the attribute for sai object
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property retriver for size"""
        return self.__size

    @property
    def position(self):
        """Property retriver for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Defining size cualifications"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        """Defining position cualifications"""
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the value of the Area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Function to print information about Square"""
        if self.__size == 0:
            print()

    if self.__position[0] >= 0 and self.__position[1] >= 0:
        for i in range(self.__position[0]):
            print()
    for j in range(self.__size):
        for k in range(self.__position[0]):
            print(" ", end='')
        for x in range(self.__size):
            print("#" * self.__size)
        print()
