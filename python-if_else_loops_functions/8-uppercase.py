#!/usr/bin/python3
def uppercase(str):
    for i in str:
        C = ord(i) > 96 and ord(i) < 123
        print("{}".format(chr(ord(i) - 32 if C else ord(i))), end="")
    print()
