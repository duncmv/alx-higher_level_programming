#!/usr/bin/python3

def uppercase(str):
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            check = 1
        else:
            check = 0
        print("{}".format(chr(ord(n) - 32)) if check == 1 else n, end='')
    print()
