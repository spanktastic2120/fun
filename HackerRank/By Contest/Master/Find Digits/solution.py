#!/bin/python

import sys

def findDigits(n):
    # Complete this function
    N = n
    count = 0
    while n > 0:
        d = n % 10
        n = n // 10
        if not d:
            continue
        count += 1 if N % d == 0 else 0
    return count

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        result = findDigits(n)
        print result

