#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda x: [y*y for y in x], matrix))
