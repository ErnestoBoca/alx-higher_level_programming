#!/usr/bin/python3
"""This module contains the Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the Square details"""
        return "[{:s}] ({:d}) {}/{} - " \
               "{}".format(self.__class__.__name__, self.id,
                           self.x, self.y, self.height)

    @property
    def size(self):
        """Gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = value
                if key == "size":
                    self.height = value
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
