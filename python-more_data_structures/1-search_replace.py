#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = my_list[:]
    for x, y in enumerate(new_l):
        if y == search:
            new_l[x] = replace
    return new_l
