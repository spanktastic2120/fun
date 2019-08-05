#!/bin/python

import sys


n = int(raw_input().strip())
for i in xrange(n):
    spaces = ''.join(' ' for _ in xrange(n-i-1))
    hashes = ''.join('#' for _ in xrange(i+1))
    print spaces+hashes
