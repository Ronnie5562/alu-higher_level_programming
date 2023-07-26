#!/usr/bin/python3
"""Defines a function to check if an obj is an instance of a given class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specific class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
