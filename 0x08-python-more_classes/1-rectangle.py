#!/usr/bin/python3
class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        initializes a rectangle
        Args:
        width - width of the rectangle
        height - height of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets the width of a rectangle"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the height of the rectangle"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
