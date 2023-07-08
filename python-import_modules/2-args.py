#!/usr/bin/python3
if __name__ == "__main__":
    """
        Outputs the number of and the list of its arguments.
    """
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))
    if length > 0:
        for arg in range(1, length + 1):
            print("{}: {}".format(arg, argv[arg]))
