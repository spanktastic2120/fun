#!/bin/python

import sys

def getWays(n, c):
    # Complete this function
    m = len(c)
    ways = [[0 for x in range(m)] for x in range(n+1)]
    
    # ways to have 0 amount for each coin denomination is 1
    for i in range(m):
        ways[0][i] = 1

    for amt in range(1, n+1):
        for denom in range(m):
            W = ways[amt - c[denom]][denom] if amt - c[denom] >= 0 else 0
            WO = ways[amt][denom - 1] if denom >= 1 else 0
            ways[amt][denom] = W + WO
    print ways[n][m-1]
    return ways[n][m-1]

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
