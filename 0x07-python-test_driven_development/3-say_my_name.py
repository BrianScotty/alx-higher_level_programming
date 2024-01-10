#!/usr/bin/python3
"""Function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints someones name

    Args:
        first_name: Person's first name
        last_name: Person's last name

    Raises:
        TypeError: if first_name or last_name is not a string

    Returns:
        My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
