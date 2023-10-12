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
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Saves the str repr into the file"""
        ls_objs = []
        if list_objs is None or len(list_objs) is 0:
            ls_objs = []
        else:
            for i in list_objs:
                ls_objs.append(i.to_dictionary())
        jsonstr = Base.to_json_string(ls_objs)
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(jsonstr)

    def from_json_string(json_string):
        """Returns a string repr of the dict"""
        if json_string is None or json_string is "":
            return "[]"
        return json.loads(json_string)
