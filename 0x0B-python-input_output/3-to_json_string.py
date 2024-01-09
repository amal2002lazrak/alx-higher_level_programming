#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing the input Python object.
    """

    return json.dumps(my_obj)
