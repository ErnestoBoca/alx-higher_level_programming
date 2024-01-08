#!/usr/bin/python3
"""My Geometry module"""


class BaseGeometry:
    """The Base Class"""
    pass

    def area(self):
        """Just raises an exception for now"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """The Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the Rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
