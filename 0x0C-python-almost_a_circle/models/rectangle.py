#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This class is a rectangle based off of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): The X position of the rectangle
            y (int, optional): The Y position of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Gets the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints out the rectangle"""
        for pos in range(self.y):
            print("")
        for x in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Prints a friendly version of the rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Updates the rectangle instance given a variable number of args"""
        if args is not None and len(args) != 0:
            alen = len(args)

            if alen >= 1:
                self.id = args[0]

            if alen >= 2:
                self.width = args[1]

            if alen >= 3:
                self.height = args[2]

            if alen >= 4:
                self.x = args[3]

            if alen >= 5:
                self.y = args[4]
        elif kwargs is not None and len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Gets the dictionary version of the rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    @property
    def x(self):
        """Getter for the private `x` attribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """Setter for the private `x` attribute"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Getter for the private `y` attribute"""
        return self.__y

    @y.setter
    def y(self, val):
        """Setter for the private `y` attribute"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    @property
    def width(self):
        """Getter for the private `width` attribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter for the private `width` attribute"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Getter for the private `height` attribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """Setter for the private `height` attribute"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val
