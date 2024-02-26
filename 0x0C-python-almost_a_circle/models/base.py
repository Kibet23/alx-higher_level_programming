#!/usr/bin/python3
"""defines the Base class"""


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
