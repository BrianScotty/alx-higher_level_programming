#!/usr/bin/python3
import json
"""Save object to a file"""

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using the 
    JSON representation.

    Args:
        my_obj: the object to write
        filename: the file to write to
    """
    with open(filename, "w", encoding="UTF=8") as f:
        json.dump(my_obj, f)
