#!/usr/bin/python3
"""
This module creates a base class for all other classes in this project
"""


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
            self.id = Base.__nb_objects
