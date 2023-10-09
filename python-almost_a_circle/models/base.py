#!/usr/bin/python3
"""
    Defining an object class named Base
"""


class Base:
    """
        Creating the attribute for said object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
