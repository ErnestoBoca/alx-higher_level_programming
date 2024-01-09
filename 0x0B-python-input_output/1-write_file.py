#!/usr/bin/python3
""""My Write file module"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
