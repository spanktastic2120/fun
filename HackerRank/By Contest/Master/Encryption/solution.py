#!/bin/python

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ","")
    l = len(s)

    # floor
    r = int(l ** 0.5)
    # ceiling
    c = int(-(-(l ** 0.5) // 1))

    out = ""
    for i in range(c):
        out += s[i::c] + " "

    return out




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
