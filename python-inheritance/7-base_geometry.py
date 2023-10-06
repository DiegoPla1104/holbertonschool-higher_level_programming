#!/usr/bin/python3
"""
    Module: area(self) integer_validator(self, name, value)
"""


class BaseGeometry:
    """
        Class BaseGeometry
    """
    def area(self):
        """Area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Name self explanatory"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
