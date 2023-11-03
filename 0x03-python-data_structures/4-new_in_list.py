#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lis = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return lis
    lis[idx] = element
    return lis
