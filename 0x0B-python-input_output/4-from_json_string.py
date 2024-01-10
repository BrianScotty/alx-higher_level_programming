#!/usr/bin/python3
"""From JSON string to object function"""
import json

def from_json_string(my_str):
    """returns an object represented by a JSON string.

    Args:
        my_str: string to represent
    """
    return json.loads(my_str)
