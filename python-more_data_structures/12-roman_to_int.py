#!/usr/bin/python3
def to_subtract(num_list):
    max_num = max(num_list)
    return max_num - sum(n for n in num_list if max_num > n)

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num, last_rom, num_list = 0, 0, [0]
    for char in roman_string:
        if char in roman_num:
            if roman_num[char] <= last_rom:
                num += to_subtract(num_list)
                num_list = [roman_num[char]]
            else:
                num_list.append(roman_num[char])
            last_rom = roman_num[char]
    return num + to_subtract(num_list)
