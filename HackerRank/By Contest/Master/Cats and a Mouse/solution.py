#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    dA = abs(z-x)
    dB = abs(z-y)
    if dA == dB:
        return "Mouse C"
    elif dA < dB:
        return "Cat A"
    return "Cat B"

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        xyz = raw_input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()
