#!/bin/python

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    print ans

if __name__ == '__main__':
    n = int(raw_input())

    extraLongFactorials(n)
