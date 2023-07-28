#!/usr/bin/python3
"""inserts a text to a file, after each line containing a search string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file based on some conditions"""
    with open(filename, 'r', encoding='UTF-8') as file:
        lns = file.readlines()

    new_lns = [ln + new_string if search_string in ln else ln for ln in lns]

    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(new_lns)
