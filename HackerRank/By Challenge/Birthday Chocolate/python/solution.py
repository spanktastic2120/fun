#!/bin/python

import sys

def solve(n, s, d, m):
    # Complete this function
    solutions = 0
    for p in range(n-m+1):
        sub = sum([s[p+i] for i in range(m)])
        solutions += 1 if sub == d else 0
    return solutions

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
