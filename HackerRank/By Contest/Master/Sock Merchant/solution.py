#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    from collections import defaultdict
    socks = defaultdict(int)
    for c in ar:
        socks[c] += 1
    return sum(socks[key]//2 for key in socks.keys())

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
