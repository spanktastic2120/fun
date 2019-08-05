#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
repeats = n//len(s)
extra = n % len(s)
rcount = 0
ecount = 0
for i, c in enumerate(s):
    if c == 'a':
        rcount += 1
        if i < extra:
            ecount += 1

count = ecount + (rcount * repeats)
print count