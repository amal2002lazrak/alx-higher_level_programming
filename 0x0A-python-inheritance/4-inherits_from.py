#!/usr/bin/python3
'''inherited class'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class that inherited'''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
