#!/usr/bin/python3
"""
    This file contains the class for a basic square
"""


class Square:
    """Class for a basic square"""

    def __init__(self, size=0, position=(0, 0)):
        """Square initializer"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the square's size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for the square's size"""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Getter for the square's position"""
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """Setter for the square's position"""
        if (not all(type(x) is int and x >= 0 for x in value) or
                len(value) is not 2 or type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if (self.__size == 0):
            print("")
        else:
            for x in range(self.position[1]):
                print("")
            for x in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
