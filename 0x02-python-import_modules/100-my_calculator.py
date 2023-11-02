#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv

    ac = len(argv) - 1
    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = "+-*/"
    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if argv[2] == '+':
        print("{} + {} = {}".format(argv[1], argv[3],
                                    calc.add(int(argv[1]), int(argv[3]))))
    elif argv[2] == '-':
        print("{} - {} = {}".format(argv[1], argv[3],
                                    calc.sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == '*':
        print("{} * {} = {}".format(argv[1], argv[3],
                                    calc.mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == '/':
        print("{} / {} = {}".format(argv[1], argv[3],
                                    calc.div(int(argv[1]), int(argv[3]))))
