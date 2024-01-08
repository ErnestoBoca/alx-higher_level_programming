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


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/7-base_geometry.txt")
