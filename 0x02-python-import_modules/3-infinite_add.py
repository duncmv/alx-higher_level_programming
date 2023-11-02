#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1;
    i , total = 1, 0
    while i <= ac:
        total = total + int(argv[i])
        i = i + 1
    print("{}".format(total))
