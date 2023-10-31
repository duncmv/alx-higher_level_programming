#!/usr/bin/python3
for n in '0123456789':
    for i in '0123456789':
        if int(i) > int(n):
            if n == '8':
                print("{}{}".format(n, i))
            else:
                print("{}{}".format(n, i), end=', ')
