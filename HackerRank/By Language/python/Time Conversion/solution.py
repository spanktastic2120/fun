#!/bin/python

import sys
import time

def timeConversion(s):
    # Complete this function
    return(time.strftime('%H:%M:%S',time.strptime(s, '%I:%M:%S%p')))

s = raw_input().strip()
result = timeConversion(s)
print(result)
