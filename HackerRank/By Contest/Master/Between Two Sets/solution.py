#!/bin/python

import sys

def getTotalX(a, b):
    # Complete this function
    return len([x for x in range(max(a), min(b)+1) if sum(x % ai for ai in a) == 0 and sum(bi % x for bi in b) == 0])
        

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
total = getTotalX(a, b)
print(total)
