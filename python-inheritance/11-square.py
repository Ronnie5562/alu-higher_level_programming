#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """A representation of a square, a special case of a rectangle with equal sides.

    Attributes:
        __size (int): The size (side length) of the square.

    Methods:
        __init__(self, size): Initialize a square instance with a given size.
        area(self): Calculate and return the area of the square.
        __str__(self): Return an informal string representation of the square.
    """

    def __init__(self, size):
        """Initialize a square instance with a given size.

        Args:
            size (int): The size (side length) of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Return an informal string representation of the square.

        Returns:
            str: A string representation of the square in the format '[Square] size/size'.
        """
        return f"[Square] {self.__size}/{self.__size}"

