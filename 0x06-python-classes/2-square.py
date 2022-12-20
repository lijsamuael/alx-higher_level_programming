#!/usr/bin/python3

""" a sqaure class"""


class Square:
    """ a class that defines private instance variables"""

    _Square__size = None

    def __init__(self, size=0):

        """The constructor of the class"""

        self._Square__size = size
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))
