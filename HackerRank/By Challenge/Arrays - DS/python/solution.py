#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
p = ' '.join(str(a) for a in arr[::-1])
print p