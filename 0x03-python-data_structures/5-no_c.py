#!/usr/bin/python3
def no_c(my_string):
    cpy = ""
    for c in my_string:
        if (c != "c" and c != "C"):
            cpy += c
    return (cpy)

