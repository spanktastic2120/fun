#!/bin/python

import sys

def patternCount(s):
    # Complete this function
    import re
    return -1 + len(re.split('10+(?=1)', s))
    

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)

