#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, j = 0, 0
    while x > 0:
        try:
            print("{:d}".format(my_list[j]), end='')
            i += 1
            j += 1
            x -= 1
        except (ValueError, TypeError):
            x -= 1
            j += 1
    print()
    return i
