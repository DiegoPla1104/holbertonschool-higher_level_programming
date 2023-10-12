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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        """Function to print the Square"""
        self.__position = [self.__x, self.__y]
        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for A in range(self.__position[1]):
                print()
        for F in range(self.__height):
            for E in range(self.__position[0]):
                print(' ', end='')
            for C in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates the values"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        if kwargs:
            k = kwargs.keys()
            for i in k:
                if i == 'id':
                    self.id = kwargs['id']
                if i == 'width':
                    self.width = kwargs['width']
                if i == 'height':
                    self.height = kwargs['height']
                if i == 'x':
                    self.x = kwargs['x']
                if i == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """Creates a dictionary and returns it"""
        
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
