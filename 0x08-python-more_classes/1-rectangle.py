#!/usr/bin/python3
"""class with private variables"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """sth"""
        self.width = width
        self.height = height

    def width(self):
        """sth"""
        return self.width

    def width(self, value):
        """sth"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.width = value

    def height(self):
        """sth"""
        return self.height

    def height(self, value):
        """sth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
