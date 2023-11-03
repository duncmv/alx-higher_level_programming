#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for i in range(len(my_string)):
        if my_string[i] not in 'cC':
            new = new + my_string[i]
    return new
