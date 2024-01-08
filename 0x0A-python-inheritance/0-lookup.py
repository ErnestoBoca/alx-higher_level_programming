#!/usr/bin/python3
"""This module contains the lookup function"""


def lookup(obj):
    """ returns the list of available attributes
    and methods of an object
    Args:
        obj: the object
    Returns:
        (list): a list object
    """
    return dir(obj)
