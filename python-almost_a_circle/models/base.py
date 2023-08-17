#!/usr/bin/python3
"""
This module creates a base class for all other classes in this project
"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file:"""
        if list_objs is None:
            json.dump([], f"{cls.__name__}.json")
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            with open('hello.json', 'w') as f:
                f.write(cls.to_json_string(list_dicts))
