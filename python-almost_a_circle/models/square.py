#!/usr/bin/python3
"""
    Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Denominator"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Property width"""
        return self.width

    @size.setter
    def size(self, value):
        """Defining size cualifications"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = self.__size

    def update(self, *args, **kwargs):
        """Updates the values"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if kwargs:
            k = kwargs.keys()
            for i in k:
                if i == 'id':
                    self.id = kwargs['id']
                if i == 'size':
                    self.width = kwargs['size']
                if i == 'x':
                    self.x = kwargs['x']
                if i == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """Creates a dictionary and returns it"""

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['x'] = self.x
        dictionary['size'] = self.width
        dictionary['y'] = self.y
        return dictionary
