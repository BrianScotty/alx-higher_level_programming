#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Defines a class Rectangle"""

class Rectangle(BaseGeometry):
    """Creates a new rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Method for the rectangle

        Args:
            width: width of rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
