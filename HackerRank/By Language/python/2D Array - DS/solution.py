#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
sums = []
for r in range(1,5):
    for c in range(1,5):
        s = arr[r-1][c-1] + arr[r-1][c] + arr[r-1][c+1]
        s += arr[r][c]
        s += arr[r+1][c-1] + arr[r+1][c] + arr[r+1][c+1]
        sums.append(s)
print max(sums)
    
