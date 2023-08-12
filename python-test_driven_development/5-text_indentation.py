#!/usr/bin/python3
"""_summary_
Write a function that prints a square with the character #.
"""


def text_indentation(text):
    """_summary_

    Args:
        text (_str_): _description: A text_

    Raises:
        TypeError: _If text is not a string_
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
