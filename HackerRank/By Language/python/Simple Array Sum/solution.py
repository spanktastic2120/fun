#!/bin/python

import sys

def simpleArraySum(n, ar):
    # Complete this function
    return sum(a for a in ar)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
