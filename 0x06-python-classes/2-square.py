#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Defines a square based on 1-square.py.

    Attributes:
        size: size of a square (1 side).
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
