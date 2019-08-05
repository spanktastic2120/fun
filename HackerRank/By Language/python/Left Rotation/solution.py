#!/bin/python

import sys

n, d = map(int, sys.stdin.readline().split(' '))
a = sys.stdin.readline().split(' ')
print ' '.join([i for i in a[d:]] + [i for i in a[:d]])


