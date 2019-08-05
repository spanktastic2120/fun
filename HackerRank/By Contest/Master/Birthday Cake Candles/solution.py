#!/bin/python

import sys
from collections import Counter

def birthdayCakeCandles(n, ar):
    # Complete this function
    c = Counter(ar)
    return c[max(c.elements())]

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
