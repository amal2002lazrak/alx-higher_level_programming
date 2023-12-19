#!/usr/bin/python3
'''define Square class'''


class Square:
    '''define its size'''

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
