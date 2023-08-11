#!/usr/bin/python3
"""_summary_
Write a function that prints a square with the character #.
"""


def print_square(size):
    """_summary_

    Args:
        size (_type_): _The size of each side of the square_

    Raises:
        TypeError: _If size is a float object and it's less than 0_
        TypeError: _If size is not an integer object_
        ValueError: _If size is less than 0_
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print('#' * size)
