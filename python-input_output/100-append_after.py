#!/usr/bin/python3
"""inserts a text to a file, after each line containing a search string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file based on some conditions"""
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        lines.extend(file.readlines())
        for index, line in enumerate(lines):
            if search_string in line:
                lines.insert(index + 1, new_string)
    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(lines)
