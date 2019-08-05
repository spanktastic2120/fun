#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
posi = nega = zero = 0
for a in arr:
    if a == 0:
        zero += 1
    elif a > 0:
        posi += 1
    else:
        nega += 1

for b in [posi, nega, zero]:
    print float(b)/n