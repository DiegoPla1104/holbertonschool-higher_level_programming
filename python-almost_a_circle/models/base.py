#!/usr/bin/python3
"""
    Defining an object class named Base
"""
import json


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

    def to_json_string(list_dictionaries):
        """Returns a string repr of the dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
