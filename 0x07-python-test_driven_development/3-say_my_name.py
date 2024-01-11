#!/usr/bin/python3
"""
this module contains the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/3-say_my_name.txt")
