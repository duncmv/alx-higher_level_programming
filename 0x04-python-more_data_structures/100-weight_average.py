#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    w_sum = 0
    w = 0
    for i in my_list:
        w_sum += i[0] * i[1]
        w += i[1]
    return w_sum / w
