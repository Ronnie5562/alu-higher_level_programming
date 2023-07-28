#!/usr/bin/python3
"""This module returns the dict represntation of a simple data struct."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
