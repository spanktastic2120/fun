#!/bin/python

import sys


t = int(raw_input().strip())
for _ in xrange(t):
    n = int(raw_input().strip())
    h = 1
    for i in xrange(n):
        if i % 2:
            h += 1
        else:
            h *= 2
    print h
