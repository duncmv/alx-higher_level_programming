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
        new = []
        for j in range(i + 1):
            if j == 0:
                new.append(1)
            elif j == i:
                new.append(1)
            else:
                new.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tri. append(new)
    return tri
