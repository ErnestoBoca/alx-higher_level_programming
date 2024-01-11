#!/usr/bin/python3
"""
this module contains the text_indentation function
"""


def text_indentation(text):
    """   prints a text with 2 new lines after each of
    these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")

    print_space = True
    for char in text:
        if char != " " or print_space:
            print(char, end="")
        print_space = True
        if char == "." or char == "?" or char == ":":
            print("\n")
            print_space = False
