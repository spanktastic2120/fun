#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #

    # sort list high to low
    keyboards = sorted(keyboards, reverse=True)
    drives = sorted(drives, reverse=True)

    # if cheapest options are too expensive still
    best = keyboards[-1] + drives[-1]
    if b < best:
        return -1
    
    # remove out-of-budget keyboards 
    for n, k in enumerate(keyboards):
        if k > b:
            continue
        keyboards = keyboards[n:]
        break

    # remove out-of-budget drives
    for n, d in enumerate(drives):
        if d > b:
            continue
        drives = drives[n:]
        break

    # for each keyboard find the most expensive drive to pair
    for k in keyboards:
        for d in drives:
            if k + d > b:
                continue
            if k + d > best:
                best = k + d
            break
        
    return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
