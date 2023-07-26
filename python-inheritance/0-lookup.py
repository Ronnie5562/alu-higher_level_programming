#!/usr/bin/python3
"""Module with a func that returns attrs and mthds of an object:."""


def lookup(obj):
    """Return a list of avail attrs nd mtds."""
    return (dir(obj))
