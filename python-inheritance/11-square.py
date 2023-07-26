#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """Initialize a square instance with a given size.

        Args:
            size (int): The size (side length) of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return an informal string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculate and return the area of the square.
        """
        return self.__size ** 2
