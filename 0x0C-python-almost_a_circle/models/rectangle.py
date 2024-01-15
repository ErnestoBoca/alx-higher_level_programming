#!/usr/bin/python3
"""This module contains the Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for lines in range(self.__y):
            print()
        for row in range(self.__height):
            print(" "*self.__x + "#" * self.__width)

    def __str__(self):
        """Returns the Rectangle details"""
        return "[{:s}] ({:d}) {}/{} - "\
               "{}/{}".format(self.__class__.__name__, self.id,
                              self.__x, self.__y,
                              self.__width, self.__height)

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer {}")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.height, self.width, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.height, self.width, self.x, self.y)
                    else:
                        self.id = value
                if key == "height":
                    self.height = value
                if key == "width":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
