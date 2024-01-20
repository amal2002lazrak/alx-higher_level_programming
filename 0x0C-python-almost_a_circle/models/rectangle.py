#!/usr/bin/python3
"""
Define Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    creates a class that represents a Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):        
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """the width attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """the width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """the height attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """the height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """the x attribute getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """the x attribute setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """the y attribute getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """the y attribute setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """a public method  that returns the area value of
        the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """a public method that prints in stdout
        the Rectangle instance with the character #
        by taking care of x and y"""
        for p in range(self.__y):
            print()
        for i in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """a public method that assigns an argument to each attribute
        or assigns a key/value argument to attributes"""
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < len(attr):
                    setattr(self, attr[idx], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """a public method  that returns
        the dictionary representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
