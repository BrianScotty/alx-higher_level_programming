#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" A square class based on 9-rectangle"""

class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """
        Method that creates a square

        Args:
            size: size of one side
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculated the area of the square
        """

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
