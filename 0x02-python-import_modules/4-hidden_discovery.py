#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lis = dir(hidden_4)
    for n in lis:
        if '__' not in n:
            print("{}".format(n))
