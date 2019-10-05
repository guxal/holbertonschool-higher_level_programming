#!/usr/bin/python3
def matrix_divided(matrix, div):
    Errortype = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(Errortype)
    _len = len(matrix[0])
    for row in matrix:
        if _len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if isinstance(x, int) is False and isinstance(x, float) is False:
                raise TypeError(Errortype)

    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    return [[float("{0:.2f}".format(x/div)) for x in row] for row in matrix]
