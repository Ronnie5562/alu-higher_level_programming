#!/usr/bin/python3
num = 122
while num > 96:
    print(chr(num) if num % 2 == 0 else chr(num - 32), end="")
    num -= 1
