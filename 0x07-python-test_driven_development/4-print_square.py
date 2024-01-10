#!/usr/bin/python3
"""Function that prints a square"""

def print_square(size):
    """
    Prints a square of '#' characters

    Args:
        size: size of each side

    Raises:
        TypeError: size input is not an integer
        ValueError: size value less than 0
        TypeError: size not greater than 0 and is a float

    Return:
        Square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
