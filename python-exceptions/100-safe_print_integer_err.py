#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as TE:
        print(f"Exception: {TE}", file=sys.stderr)
        return False
