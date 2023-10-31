#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz ", end='')
        elif n % 3 == 0 or n % 5 == 0:
            print("{} ".format("Fizz" if n % 3 == 0 else "Buzz"), end='')
        else:
            print("{} ".format(n), end='')
