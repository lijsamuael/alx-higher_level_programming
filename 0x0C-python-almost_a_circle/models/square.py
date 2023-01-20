#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is based of rectangle, but both dimensions are equal"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints a nice version of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Updates the square"""
        if args is not None and len(args) != 0:
            fin = []
            for arg in range(len(args)):
                if arg == 1:
                    fin.append(args[arg])
                fin.append(args[arg])
            super().update(*tuple(fin))
        elif kwargs is not None and len(kwargs) != 0:
            fin = {}
            for k, v in kwargs.items():
                if k == "size":
                    fin["width"] = v
                    fin["height"] = v
                else:
                    fin[k] = v
            super().update(**fin)

    def to_dictionary(self):
        """Gets the dictionary representation of the square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size (width, height) of the square"""
        super().update(width=value, height=value)
