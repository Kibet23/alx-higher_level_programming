#!/usr/bin/python3
"""defines the function First rectangle"""


from models.base import Base


class Rectangle(Base):
    """defines the class Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """defines initilization for the class Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """defines the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """defines the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """defines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        self.__height = value

    @property
    def x(self):
        """defines the argument x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        self.__x = value

    @property
    def y(self):
        """defines y"""
        return self.__y

    @y.setter
    def y(self, value):
        """defines the set value of y"""
        self.__y = value
