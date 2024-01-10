#!/usr/bin/python3
"""Append to file function."""

def append_write(filename="", text=""):
    """Appends a string to the end of the UTF8 file and returns the number
    of characters added.

    Args:
        filename: file to add to
        text: text to append
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
