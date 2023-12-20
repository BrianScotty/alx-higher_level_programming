#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    Class square based on 3-square.py.

    Attributes:
        size: size of the square.
    """
    def __init__(self, size=0):
        """Creates a new square.

        Args:
            size: size of the new square
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Return:area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
