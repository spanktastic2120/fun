#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

sums = []
for c in range(4):
    for r in range(4):
        sums.append(sum([arr[r][c], arr[r][c+1], arr[r][c+2], arr[r+1][c+1], arr[r+2][c], arr[r+2][c+1], arr[r+2][c+2]]))

print max(sums)