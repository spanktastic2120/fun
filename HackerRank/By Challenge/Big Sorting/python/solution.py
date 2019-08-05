#!/bin/python

import sys


n = int(raw_input().strip())
bucket = {}
for _ in xrange(n):
    s = sys.stdin.readline().strip()
    l = len(s)
    if l not in bucket:
        bucket[l] = []
    bucket[l].append(s)
    
for l in sorted(bucket):
    for s in sorted(bucket[l]):
        print s