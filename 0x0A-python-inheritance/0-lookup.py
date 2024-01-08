#!/usr/bin/python3
"""
define lookup function
"""


def lookup(obj):
    '''
    Return a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    list: A list of attribute and method names.
    '''
    return dir(obj)
