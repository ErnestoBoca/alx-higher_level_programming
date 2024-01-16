#!/usr/bin/python3
"""This module contains the Base Class"""
import json


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the id instance attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__
        file_name += ".json"
        with open(file_name, mode="w", encoding="utf-8") as my_file:
            if list_objs is None:
                my_file.write("[]")
            else:
                my_list = []
                for obj in list_objs:
                    my_list.append(obj.to_dictionary())
                string = cls.to_json_string(my_list)
                my_file.write(string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls(12, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, encoding="utf-8") as my_file:
                list_string = my_file.read()
                list_dict = cls.from_json_string(list_string)
                list_obj = []
                for obj in list_dict:
                    list_obj.append(cls.create(**obj))
                return list_obj
        except FileNotFoundError:
            return []
