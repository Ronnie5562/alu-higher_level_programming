#!/usr/bin/python3
"""Module with a class that contains class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    """
    return isinstance(obj, a_class)
