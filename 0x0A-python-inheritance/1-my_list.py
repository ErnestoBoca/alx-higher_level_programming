#!/usr/bin/python3
"""This module contains the MyList class"""


class MyList(list):
    """Class tha inherits from lis"""
    def print_sorted(self):
        """Prints a sorted list"""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
