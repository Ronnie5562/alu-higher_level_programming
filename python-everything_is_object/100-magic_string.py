#!/usr/bin/python3
def magic_string():
    magic_string.num = getattr(magic_string, 'num', 0) + 1
    return ("BestSchool, " * (magic_string.num - 1) + "BestSchool")
