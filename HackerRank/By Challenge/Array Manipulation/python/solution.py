#!/bin/python

import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split(' '))
M = 0
D = [0]*(n+1)
for _ in xrange(m):
    a, b, k = map(int, sys.stdin.readline().split(' '))
    D[a-1] += k
    D[b] -= k

x = 0
for i in D:
    x = x + i
    if x > M:
        M = x

print(M)
