#!/usr/bin/python3
"""Appends a string to a file and returns the num of chars written:."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        return file.write(text)
