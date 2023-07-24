#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """The Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle obj.
            height (int): The height of the rectangle obj.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property(get&set) for the width of the rectangle."""
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
        """property(get&set) for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
