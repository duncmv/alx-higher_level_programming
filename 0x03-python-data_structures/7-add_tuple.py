#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    i, j = 0, 0

    for n in tuple_a:
        a[i] = n
        i += 1
        if i > 1:
            break

    for n in tuple_b:
        b[j] = n
        j += 1
        if j > 1:
            break
    return (a[0] + b[0], a[1] + b[1])
