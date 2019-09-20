#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix is None:
        return 0
    return list(map(lambda e: list(map(lambda i: i**2, e)), matrix))
