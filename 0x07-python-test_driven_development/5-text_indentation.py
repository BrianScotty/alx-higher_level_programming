#!/usr/bin/python3
"""Function that prints 2 lines after certain characters"""

def text_indentation(text):
    """
    Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.

    Args:
        text: text to print

    Raises:
        TypeError: text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
