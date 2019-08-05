#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    highs = lows = 0
    highest = lowest = s[0]
    for i in s[1:]:
        if i > highest:
            highest = i
            highs += 1
        elif i < lowest:
            lowest = i
            lows += 1
    return highs, lows

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
