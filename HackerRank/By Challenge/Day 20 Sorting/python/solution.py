#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
swapsTotal = 0
for _ in a:
    swaps = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            swaps += 1
    swapsTotal += swaps
    if not swaps:
        break
        
print "Array is sorted in %s swaps." % swapsTotal
print "First Element: %s" % a[0]
print "Last Element: %s" % a[-1]
            