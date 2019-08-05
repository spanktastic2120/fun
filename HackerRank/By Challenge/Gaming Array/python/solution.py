#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    loc = {e:i for i,e in enumerate(arr)}
    order = sorted(arr)
    pos = loc[order.pop()]
    if pos == 0:
        return "BOB"
    turn = 1
    while pos:
        n = loc[order.pop()]
        print n
        if n < pos:
            pos = n
            turn *= -1

    if turn < 0:
        return "ANDY"
    return "BOB"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(raw_input().strip())

    for g_itr in xrange(g):
        arr_count = int(raw_input().strip())

        arr = map(int, raw_input().rstrip().split())

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
