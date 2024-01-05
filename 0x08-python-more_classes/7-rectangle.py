#!/usr/bin/python3
"""This module contains a Rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle shape"""
        if self.__height == 0 or self.__width == 0:
            return ""
        msg = ""
        for i in range(self.__height):
            for j in range(self.__width):
                msg += str(self.print_symbol)
            if i != self.__height - 1:
                msg += "\n"
        return msg

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
