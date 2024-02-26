#!/usr/bin/python3
"""defines the function First rectangle"""


from models.base import Base


class Rectangle(Base):
    """defines the class Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """defines initilization for the class Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the new rectangle
            y (int): y coordinate of the new rectangle
        """

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """defines the argument x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """defines y"""
        return self.__y

    @y.setter
    def y(self, value):
        """defines the set value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """defines the area of the rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the rectangle instance with char #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """overrides the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height)
