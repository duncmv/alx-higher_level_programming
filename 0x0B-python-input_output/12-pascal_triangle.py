#!/usr/bin/python3
"""defines pascal_triangle function"""


def pascal_triangle(n):
    """"returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    tri = []
    if n <= 0:
        return tri

    for i in range(n):
        new = [1]
        if i > 1:
            for j in range(1, i):
                new.append(tri[i - 1][j - 1] + tri[i - 1][j])
        if i > 0:
            new.append(1)
        tri. append(new)
    return tri
