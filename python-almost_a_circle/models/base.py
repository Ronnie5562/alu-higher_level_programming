#!/usr/bin/python3
"""
This module creates a base class for all other classes in this project
"""
import os
import csv
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
        """to json string"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        f_name = f"{cls.__name__}.json"
        with open(f_name, "w") as f:
            if list_objs:
                list_of_dict = [obj.to_dictionary() for obj in list_objs]
            else:
                list_of_dict = []
            f.write(cls.to_json_string(list_of_dict))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = f"{cls.__name__}.json"
        list_of_instances = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                list_dicts = cls.from_json_string(my_file.read())
                list_of_instances = [cls.create(**dic) for dic in list_dicts]
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
