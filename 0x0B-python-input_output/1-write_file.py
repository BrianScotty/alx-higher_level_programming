#!/usr/bin/python3
"""Write to file function"""

def write_file(filename="", text=""):
    """Method that writes input to the file UTF8 and returns
    the number of characters written.
    Args:
        filename: name of file to write to
        text: input to write to file

    Returns:
        number of characters written.
    """

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
