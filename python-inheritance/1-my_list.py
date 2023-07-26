#!/usr/bin/python3
"""Creates a Mylist class that inherits from list."""


class MyList(list):
    """Mylist class => A sub class of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
