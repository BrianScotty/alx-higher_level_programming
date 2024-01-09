#!/usr/bin/python3
"""Class MyInt inherited from int."""

class MyInt(int):
    """A rebel class that inverts operators."""

    def __eq__(self, value):
        """"
        Change the operation of == to !=
        """
        return self.real != value

    def __ne__(self, value):
        """
        Change the operation of != to ==
        """
        return self.real == value
