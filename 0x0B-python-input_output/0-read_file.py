#!/usr/bin/python3
"""Module with a function that reads a text file."""

def read_file(filename=""):
    """Method that reads the text in file UTF8 and it to stdout"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
