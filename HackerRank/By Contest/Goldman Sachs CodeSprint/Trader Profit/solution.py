#!/bin/python

import sys

def traderProfit(k, n, A):
    # Complete this function

    profit = {}
    for i in range(k+1):
        profit[(i, 0)] = 0
    for i in range(n+1):
        profit[(0, i)] = 0

    for i in range(1, k+1):
        prev = -9999
        for j in range(1, n):
            prev = max(prev, profit[(i-1, j-1)] - A[j-1])
            profit[(i, j)] = max(profit[(i, j-1)], A[j] + prev)

    return profit[(k, n-1)]
    

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        k = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = traderProfit(k, n, arr)
        print result

