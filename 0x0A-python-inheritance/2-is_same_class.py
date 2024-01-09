#!/usr/bin/python3
"""module that checks if an object is an instance of a class"""

def is_same_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    
    Args:
        obj: object to check
        a_class: class to check if the object is part of it

    Return:
        True - object is exactly an instance of the specified class
        False - if not
    """

    if type(obj) == a_class:
        return True
    return False
