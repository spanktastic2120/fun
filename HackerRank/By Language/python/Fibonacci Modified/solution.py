#!/bin/python

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    if n == 1: return t1
    if n == 2: return t2
    if n == 3: return (t2**2 + t1)
    return fibonacciModified(t1, t2, n-1)**2 + fibonacciModified(t1, t2, n-2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = raw_input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
