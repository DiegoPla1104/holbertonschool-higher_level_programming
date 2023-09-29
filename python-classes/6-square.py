#!/usr/bin/python3
"""
    Square Class Object
"""
class Square():
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Square "Function" parameters"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
    @property
    def size(self):
        """Size retriever"""
        return self.__size
    @size.setter
    def size(self, value):
        """Size parameters"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        """Position retriever"""
        return self.__position
    @position.setter
    def position(self, value):
        """Position parameters"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        """Area of the Square"""
        return self.__size * self.__size
    def my_print(self):
        """Function to print the Square"""
        if self.__size == 0:
            print()
            return
        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for A in range(self.__position[1]):
                print()
        for F in range(self.__size):
            for E in range(self.__position[0]):
                print(' ', end='')
            for C in range(self.__size):
                print('#', end='')
            print()
