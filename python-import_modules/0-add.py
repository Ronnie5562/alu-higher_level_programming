#!/usr/bin/python3
if __name__ == "__main__":
    """
        imports the function def add(a, b): from the file add_0.py\
                and prints the result of the addition 1 + 2 = 3
    """
    from add_0 import add
    a, b = 1, 2
    print("{} + {} = {}".format(a, b, add(a, b))
