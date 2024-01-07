#!/usr/bin/python3
"""this function adds two integers a and b
if one of the integers is a float it turn it to integer
if one of the integers is not int it raises a TypeError
b is set to 98 by default
Returns the sum of the two integers"""


def add_integer(a, b=98):
    """chekcs if there was an Error with the integers
    it raises a Type Error or it changes it to an integer
    otherwise it returns the sum"""
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
