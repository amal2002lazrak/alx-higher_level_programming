#!/usr/bin/python3
"""s Base that refer to the base class of other classes"""
import json
import csv
import os


class Base:
    """A base class for other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the JSON string
        representation of list_objs to a file"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dictionary = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """a static method that returns the list of the
        JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a class method that returns an instance
        with all attributes already set (using a "dummy")"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """a class method that returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                file_dt = f.read()
                if not file_dt:
                    return []
                json_list = cls.from_json_string(file_dt)
                return_list = []
                for item in json_list:
                    return_list.append(cls.create(**item))
                return return_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of list of objects"""
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "square":
                    attrs = ["id", "size", "x", "y"]
                csv_file = csv.DictWriter(f, attrs=attrs)
                for item in list_objs:
                    csv_file.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from cxv file"""
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                ld = csv.DictReader(f, fieldnames=fieldnames)
                ld = [{key: int(value) for key, value in dictionary.items()}
                      for dictionary in ld]
                return [cls.create(**dictionary) for dictionary in ld]
        except FileNotFoundError:
            return []
