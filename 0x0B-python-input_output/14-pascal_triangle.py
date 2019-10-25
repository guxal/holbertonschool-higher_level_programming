#!/usr/bin/python3
"""
This method contains the function pascal_triangle
"""


def pascal_triangle(n):
    """
    This function return pascal triangle
    """
    triangle = []
    row = [1]
    k = [0]
    for i in range(n):
        triangle.append(row)
        row = [val1+val2 for val1, val2 in zip(row+k, k+row)]
    return triangle
