#!/bin/python

import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.
def flippingMatrix(matrix):
    n = len(matrix[0]) / 2
    best = 0
    for i in range(n):
        for j in range(n):
            best += max([
                matrix[i][j],
                matrix[2*n-1 - i][j],
                matrix[2*n-1 - i][2*n-1 - j],
                matrix[i][2*n-1 - j]
            ])
    return best

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        matrix = []

        for _ in xrange(2*n):
            matrix.append(map(int, raw_input().rstrip().split()))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
