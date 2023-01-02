#!/usr/bin/python3
"""class with private variables"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """sth"""
        self._Rectangle_width = width
        self._Rectangle_height = height

    @property
    def width(self):
        """sth"""
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        """sth"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle_width = value

    @property
    def height(self):
        """sth"""
        return self._Rectangle_height

    @height.setter
    def height(self, value):
        """sth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle_height = value
