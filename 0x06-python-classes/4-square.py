#!/usr/bin/python3

""" a sqaure class"""


class Square:
    """ a class that defines private instance variables"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    _Square__size = None
    
    @size.setter
    def size(self, size=0):

        """The constructor of the class"""

        self._Square__size = size
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))

    def area(self):
        return self._Square__size ** 2
