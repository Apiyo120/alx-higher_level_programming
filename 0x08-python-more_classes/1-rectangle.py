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
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrives the height"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
