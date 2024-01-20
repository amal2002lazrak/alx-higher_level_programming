#!/usr/bin/python3
"""a Square class that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """defining the attributes of the Class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """the size attribute getter"""
        return self.width

    @size.setter
    def size(self, value):
        """the size attribute setter"""
        self.width = value

    def __str__(self):
        """The overloading __str__ method should return
        [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """a public method that assigns attributes"""
        attr = ["id", "size", "x", "y"]
        if args:
            for indx, value in enumerate(args):
                if indx < len(attr):
                    setattr(self, attr[indx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """a public method that returns
        the dictionary representation of a Square"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
