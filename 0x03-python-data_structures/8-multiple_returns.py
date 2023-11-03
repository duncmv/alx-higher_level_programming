#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    return lent, None if lent == 0 else sentence[0]
