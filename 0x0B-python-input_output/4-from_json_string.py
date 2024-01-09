#!/usr/bin/python3
"""
a function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Parses a JSON-formatted string and converts it into a Python object.

    Args:
        my_str (str): The JSON-formatted string to be parsed.

    Returns:
        obj: A Python object representing the parsed JSON data.
    """

    return json.loads(my_str)
