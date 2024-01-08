#!/usr/bin/python3
"""My MyInt module"""


class MyInt(int):
    """The MyInt Class"""
    def __eq__(self, other):
        """Inverts the operator =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the operator !="""
        return super().__eq__(other)
