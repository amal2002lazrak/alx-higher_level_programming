#!/usr/bin/python3
"""
a function that returns True if the object is exactly
an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclasses.
    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to check for object membership.

    Returns:
    bool: True if 'obj' is an instance of 'a_class' or
    its subclasses, False otherwise.
    """

    if type(obj) == a_class:
        return True

    return False
