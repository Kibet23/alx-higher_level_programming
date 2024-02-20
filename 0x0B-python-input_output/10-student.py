#!/usr/bin/python3
"""defines Student to JSON with filter"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes student name with first_name, last_name andd age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retreives a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
