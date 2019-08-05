#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    from itertools import combinations
    combos = combinations(ar, 2)
    return sum([1 for l, r in combos if (l+r)%k == 0])
    

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
