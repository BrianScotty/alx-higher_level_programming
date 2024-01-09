#!/usr/bin/python3
"""module that checks instance or inherited instance"""

def is_kind_of_class(obj, a_class):
    """
    Method that checks if object is an actual or inherited instance of a class

    Args:
        obj: object to check
        a_class: class to check

    Return:
        True: If instance or inherited instance
        False: if not
    """

    if isinstance(obj, a_class):
        return True
    return False
