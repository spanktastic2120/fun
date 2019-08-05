#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if p == 1:
        return 0
    if p == n and n % 2 == 0:
        return 0
    
    front = p // 2
    back = (n - p + 1) // 2 if n % 2 == 0 else (n - p) // 2
    return min([front, back])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = int(raw_input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
