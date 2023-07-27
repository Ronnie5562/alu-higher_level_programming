#!/usr/bin/python3
"""writes a string to a file and returns the num of chars written:"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
