#!/bin/python

import sys
from itertools import combinations

arr = map(int, raw_input().strip().split(' '))
combos = combinations(arr, 4)
maximum = 1
minimum = 5*10**9
for c in combos:
    s = sum(c)
    if s > maximum:
        maximum = s
    if s < minimum:
        minimum = s

print minimum, maximum