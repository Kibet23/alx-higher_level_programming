#!/usr/bin/python3
"""defines the function with the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the class square inherited from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the function used to define the class Square
        Args:
            self: the square
            size (int): the size of the square
            id (int): identity of the square
            x (int): x coordinate of the square
            y (int): y coordnate of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """define the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the class Square by adding it that assigns attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """defines dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """defines string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
