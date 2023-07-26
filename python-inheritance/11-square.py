#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """A representation of a square
    """
    def __init__(self, size):
        """instantiation of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
