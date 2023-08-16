#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for heigth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for row in range(self.__y):
            print("")
        for row in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args):
        """assigns an argument to each attribute:"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            self.__init__(self.width, self.height, self.x, self.y)
            for arg in range(1, args):
                self.attr[arg] = args[arg]

    def __str__(self):
        """String representation of a rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
