#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """The Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property(get&set) for the width of the Rectangle."""
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
        """property(get&set) for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        output = []
        for x in range(self.__height):
            [output.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                output.append('\n')
        return "".join(output)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        string = f"Rectangle({str(self.__width)}, {str(self.__height)})"
        return string
