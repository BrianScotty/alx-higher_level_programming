#!/usr/bin/python3
"""A class called BaseGeometry"""

class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """method to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that checks if value is an integer

        Args:
            name: assume as always a string
            value: input value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is equal to or less than 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
