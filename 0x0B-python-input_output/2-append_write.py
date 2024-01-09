#!/usr/bin/python3
"""My append module"""


def append_write(filename="", text=""):
    """Appends a text to a file"""
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
