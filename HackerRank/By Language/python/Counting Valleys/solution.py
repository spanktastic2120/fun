#!/bin/python

import sys

def countingValleys(n, s):
    # Complete this function
    height = 0
    valleys = 0
    for step in s:
        prev = height
        height += 1 if step == 'U' else -1
        #print step, height
        if prev == 0 and height == -1:
            valleys += 1
    return valleys

if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    result = countingValleys(n, s)
    print result
