#!/bin/python

import sys


t = int(raw_input().strip())
for _ in xrange(t):
    n,k = map(int, raw_input().strip().split(' '))
    print k-1 if ((k-1) | k) <= n else k-2