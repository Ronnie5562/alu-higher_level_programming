#!/usr/bin/python3
"""_summary_
Write a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (_type_): _User first name_
        last_name (str, optional): _User last name_. Defaults to "".

    Raises:
        TypeError: _if first_name is not a string_
        TypeError: _if last_name is not a string_

    Returns:
        _str_: _My name is {first_name} {last_name}_
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
