#!/usr/bin/python3
def max_integer(my_list=[]):
    lis = len(my_list)
    if lis == 0:
        return
    m = my_list[1]
    for n in my_list:
        if n > m:
            m = n
    return m
