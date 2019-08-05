#!/bin/python3

import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split(' '))
M = 0
D = defaultdict(int)
for _ in range(m):
    a, b, k = map(int, sys.stdin.readline().split(' '))
    D[a] += k
    D[b+1] -= k

x = 0
for i in range(1, n+1):
    x = x + D[i]
    if x > M:
        M = x

print(M)
