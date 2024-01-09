#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Reads and parses JSON data from a specified file.

    Args:
        filename (str): The name of the JSON file to be read and parsed.

    Returns:
        dict or list: A Python dictionary or list representing the
        parsed JSON data.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
