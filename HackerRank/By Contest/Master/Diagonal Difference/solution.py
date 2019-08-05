#!/bin/python

import sys


n = int(raw_input().strip())
primary = 0
secondary = 0
for i in xrange(n):
    row = map(int,raw_input().strip().split(' '))
    primary += row[i]
    secondary += row[n-i-1]
print abs(primary - secondary)
