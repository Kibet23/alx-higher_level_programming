#!/usr/bin/python3
"""defines a function for the class to JSON"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a student with first name, last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retreives a dictionary representation of a student instance"""
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
