#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nl = []
    for n in my_list:
        if n % 2 == 0:
            nl.append(True)
        else:
            nl.append(False)
    return nl
