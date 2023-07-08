#!/usr/bin/python3
def remove_char_at(str, n):
    x = str[:n] + str[n + 1:] if n >= 0 else str
    return x
