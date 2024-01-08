#!/usr/bin/python3
"""
a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
     This function determines whether the given object, 'obj',
     is an instance of the specified class 'a_class'
    or any of its subclasses, considering inheritance relationships.

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to check for object membership
    and its subclasses.

    Returns:
    bool: True if 'obj' is an instance of 'a_class' or
    any of its subclasses, False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    return False
