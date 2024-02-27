#!/usr/bin/python3
"""defines the Base class"""
import json


class Base:
    """defines the class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the constructor for the class Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
