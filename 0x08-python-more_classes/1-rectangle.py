#!/usr/bin/python3
"""class with private variables"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """sth"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """sth"""
        return self._width

    @width.setter
    def width(self, value):
        """sth"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self._width = value

    @property
    def height(self):
        """sth"""
        return self._height

    @height.setter
    def height(self, value):
        """sth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
