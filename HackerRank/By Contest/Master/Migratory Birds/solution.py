#!/bin/python

import sys

def migratoryBirds(n, ar):
    # Complete this function
    one = two = three = four = five = 0
    for b in ar:
        if b == 1:
            one += 1
        elif b == 2:
            two += 1
        elif b == 3:
            three += 1
        elif b == 4:
            four += 1
        else:
            five += 1
    counts = sorted([(one, 1), (two, 2), (three, 3), (four, 4), (five, 5)], reverse=True)
    high = counts[0][1]
    for i in range(4):
        if counts[i][0] == counts[i+1][0]:
            high = min([counts[i][1], counts[i+1][1]])
        else:
            break
    return high
        
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
