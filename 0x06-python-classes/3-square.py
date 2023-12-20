#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Square based on 2-square.py.

    Attributes:
        size: size of square.
    """
    def __init__(self, size=0):
        """Creates a new square.

        Args:
            size: size of the new square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area the square.

        Return: the area of the new square.
        """
        return self.__size ** 2
