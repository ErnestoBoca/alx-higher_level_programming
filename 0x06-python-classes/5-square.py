#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """The Square class"""
    def __init__(self, size=0):
        """Initializes a Square with its size
        Args:
            self: the object
            size(int): the size of the square
        """
        if (type(size)) == int:
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """Return the size of the square
            Returns:
                int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Setters the size of the square
            Args:
                size(int): the size of the square
        """
        if (type(size)) == int:
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of a square
            Returns:
                int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with character
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if (self.__size == 0):
            print()
