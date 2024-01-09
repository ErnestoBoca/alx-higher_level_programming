#!/usr/bin/python3
"""My reaad_file module"""


def read_file(filename=""):
    """Reads a text from a file"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
