#!/usr/bin/python3
if __name__ == "__main__":
    """
        Prints the addition of all arguments
    """
    from sys import argv
    ans = 0
    for arg in range(1, len(argv)):
        ans += int(argv[arg])
    print(ans)
