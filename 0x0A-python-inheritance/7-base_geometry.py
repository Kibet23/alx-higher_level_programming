#!/usr/bin/python3
"""defines the integer validator from the BaseGeometry class"""


class BaseGeometry:
    """defines the class BaseGeometry"""

    def area(self):
        """defines the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            self: to be value
            name: name of the integer to be value
            value: amount of validity
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
