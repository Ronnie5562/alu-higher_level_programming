#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class defines the blueprint for a Square object """

    def __init__(self, size, x=0, y=0, id=None):
        """ This func initializes a Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The string representation of a Square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size [width / height] of the square"""
        return self.width if self.width else self.height

    @size.setter
    def size(self, value):
        """Sets the size [width / height] of the square"""
        self.width = value
        self.height = value
