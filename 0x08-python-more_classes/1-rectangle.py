#!/usr/bin/python3
"""class with private variables"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """sth"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """sth"""
        return self.__Rectangle_width

    @width.setter
    def width(self, value):
        """sth"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__Rectangle_width = value

    @property
    def height(self):
        """sth"""
        return self.__Rectangle_height

    @height.setter
    def height(self, value):
        """sth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__Rectangle_height = value
