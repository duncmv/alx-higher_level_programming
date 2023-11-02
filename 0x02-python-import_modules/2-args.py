#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    print("{} {}{}".format(ac, "argument" if ac == 1 else "arguments",
                           "." if ac == 0 else ":"))
    i = 1
    while i <= ac:
        print("{}: {}".format(i, argv[i]))
        i = i + 1
