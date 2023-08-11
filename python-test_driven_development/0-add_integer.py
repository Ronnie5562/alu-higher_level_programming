#!/usr/bin/python3
"""_summary_
This module returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """_summary_

    Args:
        a (_type_): _description_
        b (int, optional): _description_. Defaults to 98.

    Raises:
        TypeError: __if a is neither an int or float object__
        TypeError: __if b is neither an int or float object__

    Returns:
        _type_: __The addition of a and b__
    """

    if not (isinstance(a, int)) and not (isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)) and not (isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
