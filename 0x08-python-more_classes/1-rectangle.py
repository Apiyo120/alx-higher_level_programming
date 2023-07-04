#!/usr/bin/python3

class Rectangle:
    """A class that is representing a rectangle.
    Attributes:
    width (int): This is the width of a rectangle.
    height (int): This is the height of a rectangle.
    """

    def __init__(self, width=0, height=0):
        """It initializes rectangle instance with optional width and height.
        Args:
        width (int): This is the width of a rectangle. It defaults to 0.
        height (int): This is the height of a rectangle. It defaults to 0.
        """

        self.width = 0
        self.height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is a getter method to retrieve the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """This is a setter method to set the width of a rectangle.
        Args:
        value (int): This is the width value to set.

        Raises:
        TypeError: If the provided width is not an integer.
        ValueError: If the provided width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """This is a getter method to retrieve the height of a rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """This is a setter method to set the height of the rectangle.

        Args:
        value (int): The height value to set.

        Raises:
        TypeError: This is if the provided height is no an integer.
        ValueError: This is if the provided height is less than 0.
        """

        if not instance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

rectangle = Rectangle()
print(rectangle.width)
print(rectangle.height)
