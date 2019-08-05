#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
jumps = 0
i = 0

while i < n-2:
    if not c[i+2]:
        i += 2
    else:
        i += 1
    jumps += 1

if i < n-1:
    jumps += 1

print jumps