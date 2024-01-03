#!/usr/bin/python3
"""
    my addition module
"""


def add_integer(a, b=98):
    """ Adds two integers values """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

if __name__ == "__main__":
    import docset
    docset.testfile("./test/0-add_integer.txt")
