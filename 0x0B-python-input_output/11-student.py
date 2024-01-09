#!/usr/bin/python3
""""Student JSON module"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
            try:
                new_dict[attr] = self.__dict__[attr]
            except KeyError:
                pass

        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.__dict__ = json
