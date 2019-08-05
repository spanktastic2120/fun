#!/bin/python

import sys

def beautifulDays(i, j, k):
    # Complete this function
    count = 0
    for n in range(i, j+1):
        N = n
        rev = 0
        while n > 0:
            r = n % 10
            n = n // 10
            rev = (rev * 10) + r
        count += 1 if abs(N - rev) % k == 0 else 0
    
    return count

if __name__ == "__main__":
    i, j, k = raw_input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print result
