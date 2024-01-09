#!/usr/bin/python3
"""This module contains the load_from_json_file function"""


import json


def load_from_json_file(filename, encoding="utf-8"):
    """ creates an Object from a JSON file"""
    with open(filename) as my_file:
        return json.load(my_file)
