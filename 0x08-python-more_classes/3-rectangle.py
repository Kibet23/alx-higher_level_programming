#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
            width: width of the new rectangle
            height: height of the new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """sets the width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""

        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter area"""

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return the printable presentation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
