#!/bin/python

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    words = ""
    num = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
            6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
            11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
            15:"quarter", 16:"sixteen", 17:"seventeen", 18:"eighteen",
            19:"nineteen", 20:"twenty", 30:"half"}
    if m == 0:
        # o'clock
        words = num[h] + " o' clock"
    else:
        if m <= 30:
            if m == 1:
                words = num[m] + " minute past "
            elif m == 15:
                words = num[m] + " past "
            elif m < 21:
                words = num[m] + " minutes past "
            elif m < 30:
                words = num[20] + " " + num[m%10] + " minutes past "
            else:
                words = "half past "
            words = words + num[h]
        else:
            if m == 59:
                words = num[1] + " minute to "
            elif m == 45:
                words = num[15] + " to "
            elif m > 39:
                words = num[60-m] + " minutes to "
            else:
                words = num[20] + " " + num[(m%10)] + " minutes to "
            words = words + num[(h%12)+1]
    return words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(raw_input())

    m = int(raw_input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
