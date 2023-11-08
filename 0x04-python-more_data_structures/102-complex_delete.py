#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lis = []
    for n in a_dictionary:
        if a_dictionary[n] == value:
            lis.append(n)
    for n in lis:
        del a_dictionary[n]
    return a_dictionary
