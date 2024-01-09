#!/usr/bin/python3
"""Module with class MyList"""

class MyList(list):
    """My MyList class"""

    def print_sorted(self):
        """Sorts a list in ascending order"""

        print(sorted(list(self)))
