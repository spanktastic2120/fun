#!/bin/python

import sys

def onceInATram(x):
    # Complete this function
    y = x+1
    L = sum(int(i) for i in str(y)[:3])
    R = sum(int(i) for i in str(y)[3:])
    while L != R:
        y += 1
        L = sum(int(i) for i in str(y)[:3])
        R = sum(int(i) for i in str(y)[3:])
    return y


if __name__ == "__main__":
    x = int(raw_input().strip())
    result = onceInATram(x)
    print result
