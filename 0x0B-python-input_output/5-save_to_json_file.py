#!/usr/bin/python3
"""
Write a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes a Python object and saves it to a JSON file.

    Args:
        my_obj: The Python object to be serialized and saved to the file.
        filename (str):
        The name of the JSON file where the object will be saved.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
