#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    Represents a student with first name, last name, and age attributes.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(): Converts the Student object to a JSON-compatible dictionary.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(type(x) == str for x in attrs):
            new_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
