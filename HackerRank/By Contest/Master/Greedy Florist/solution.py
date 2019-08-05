#!/bin/python

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k == len(c):
        return sum(c)
    c = sorted(c)
    f = len(c)
    cost = 0
    mult = 0
    while c:
        for x in range(k):
            if c: cost += (1 + mult) * c.pop()
        mult += 1
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
