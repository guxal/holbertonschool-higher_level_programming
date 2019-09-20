#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda e: list(map(lambda i: i**2, e)), matrix))
