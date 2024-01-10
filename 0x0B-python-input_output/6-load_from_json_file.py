#!/usr/bin/python3
"""Create object from a JSON file"""
import json

def load_from_json_file(filename):
    """
    Method that creates an object from a JSON file

    Args:
        filename: name of the JSON file
    """
    with open(filename) as f:
        return json.load(f)
