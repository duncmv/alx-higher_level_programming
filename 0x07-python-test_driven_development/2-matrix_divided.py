#!/usr/bin/python3
"""
This a module that defines a function matrix_divided
It checks for the element types of the matrix
It also checks for the size of the rows of the matrix
also checks the type of the divisor and if its 0
"""


def matrix_divided(matrix, div):
    """
    This is the matrix divide function described
    """

    err1 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(err1)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(err1)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(err1)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for row in matrix:
        new.append(list(map(lambda n: round(n / div, 2), row)))

    return new
