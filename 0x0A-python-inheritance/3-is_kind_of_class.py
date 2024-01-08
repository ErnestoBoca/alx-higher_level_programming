#!/usr/bin/python3
"""This module contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """True if the object is an instance of, or
    if the object is an instance of a class that inherited from,
    the specified class ; otherwise False"""
    return isinstance(obj, a_class)
