#!/usr/bin/python3
for n in 'abcdefghijklmnopqrstuvwxyz':
    if n == 'q' or n == 'e':
        continue
    print("{}".format(n), end='')
