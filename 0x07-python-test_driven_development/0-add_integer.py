#!/usr/bin/python3
"""
    my addition module
"""


def add_integer(a, b=98):
    """ Adds two integers values
    Args:
        a (int): the first value
        b (int): the second value
    Returns:
        int: the sum of two values
    Raises:
        TypeError: if a or b is not an integer
    """
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
