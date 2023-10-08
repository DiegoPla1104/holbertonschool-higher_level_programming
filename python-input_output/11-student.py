#!/usr/bin/python3
"""
    Class Student that defines
    a student by: (based on 10-student.py)
"""


class Student:
    """
        Class student
    """

    def __init__(self, first_name, last_name, age):
        """
            init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            To json
        """
        if type(attrs) is list:
            c = {}
            for a in attrs:
                if a in self.__dict__:
                    c[a] = self.__dict__[a]
            return lib

        return self.__dict__

    def reload_from_json(self, json):
        """
            Reload
        """
        for a, b in json.items():
            self.__dict__[a] = b
