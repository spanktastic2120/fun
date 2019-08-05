#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count = dict()
    for i in a:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    keys = sorted(count.keys())
    best = 0
    for i in range(len(keys) - 1):
        run = 0
        if keys[i+1] - keys[i] > 1:
            run = count[keys[i]]
        else:
            run = count[keys[i]] + count[keys[i+1]]
        if run > best:
            best = run
    if count[keys[-1]] > best:
        return count[keys[-1]]
    else:
        return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
