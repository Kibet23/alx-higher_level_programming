#!/usr/bin/python3
"""defines Student to disk and reload"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initilaizes the first name, last name and age"""
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

    def reload_from_json(self, json):
        """replaces all attributes of thee Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
