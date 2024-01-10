#!/usr/bin/python3
"""Module that adds two integers"""

def add_integer(a, b=98):

    """Adds two integers.

    Args:
        a: first integer.
        B: second integer set to equal 98.

    Raises:
        TypeError: if a or b are neither an int nor a float.

    Return:
        sum of a and b.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
