#!/bin/python3

import sys


n = int(sys.stdin.readline().strip())
bucket = {}
for _ in range(n):
    s = sys.stdin.readline().strip()
    l = len(s)
    if l not in bucket:
        bucket[l] = []
    bucket[l].append(s)
    
for l in sorted(bucket):
    for s in sorted(bucket[l]):
        print(s)