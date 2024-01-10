#!/usr/bin/python3
"""To JSON string function"""
import json

def to_json_string(my_obj):
    """Returns a JSON representation of an object

    Args:
        my_obj: object to use
    """
    return json.dumps(my_obj)
