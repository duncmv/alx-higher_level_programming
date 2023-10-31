#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = number % -10
str1 = 'Last digit of'
str5 = 'and is greater than 5'
str0 = 'and is 0'
str6 = 'and is less than 6 and not 0'
if last > 5:
    print(str1, number, 'is', last, str5)
elif last == 0:
    print(str1, number, 'is', last, str0)
elif last < 6 and last != 0:
    print(str1, number, 'is', last, str6)
