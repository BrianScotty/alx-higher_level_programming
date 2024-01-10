#!/usr/bin/python3
"""Class to JSON"""

def class_to_json(obj):
    """
    Funtion that returns the dictionary description
    with simple data structure

    Args:
        obj: instance of a class
    """

    return obj.__dict__
