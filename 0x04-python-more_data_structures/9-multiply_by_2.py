#!/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for k, v in a_dictionary.items():
        new[k] = 2 * v
    return (new)
