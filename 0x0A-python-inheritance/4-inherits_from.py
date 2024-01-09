#!/usr/bin/python3
"""module that checks if object is inherited directly or indirectly"""

def inherits_from(obj, a_class):
    """
    Method that checks if an object is an instance of a class that 
    inherited directly or indirectly

    Args:
        obj: the object
        a_class: the class

    Return:
        True: if object is inherited
        False: if not
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
