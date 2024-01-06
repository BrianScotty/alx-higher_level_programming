#!/usr/bin/python3
"""Rectangle based on 0-rectangle
"""

class Rectangle:
    """1-rectangle

    Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): width of the rectangle
            """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value (int): size value

        Attributes:
            __width (int): width of the rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): size value

        Attributes:
            __height (int): height of the rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
