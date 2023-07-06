#!/usr/bin/python3


"""Define a class rectangle"""


class Rectangle:
    """An attempt to create a rectngle"""
    def __init__(self, width=0, height=0):
        """Initialises the attirbuutes."""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrives the width"""
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
        """Retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return = 0

        return ((self.__width * 2) + (self.__height * 2))
