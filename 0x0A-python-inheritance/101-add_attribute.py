#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible

    Args:
        obj: the object to add to
        att: the attribute
        value: value of the attribute

    Raises:
        TypeError: attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
