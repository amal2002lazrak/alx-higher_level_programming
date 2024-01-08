#!/usr/bin/python3
"""
a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Public instance method: def area(self):
    that raises an Exception with the message area()
    is not implemented
    """

    def __init__(self, width, height):
        '''
        width and height must be positive integers
        '''

        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}" .format(self.__width, self.__height)
