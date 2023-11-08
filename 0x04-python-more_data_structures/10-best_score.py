#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    m = 0
    for n in a_dictionary:
        if a_dictionary[n] > m:
            best = n
    return best
