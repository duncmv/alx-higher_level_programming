#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new = []
    for i in matrix:
        new_row = list(map(lambda x: x ** 2, i))
        new.append(new_row)
    return new
