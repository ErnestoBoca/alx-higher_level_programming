#!/usr/bin/python3
""""My Write file module"""


def write_file(filename="", text=""):
    """"Writes tect into a file and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
