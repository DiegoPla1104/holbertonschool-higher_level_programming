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
