#!/bin/python

import sys

def countingSort(arr):
    # Complete this function
    count = [0 for x in range(100)]
    ret = []
    for i in arr:
        count[i] += 1
    for i,r in enumerate(count):
        for j in range(r):
            ret.append(i)
    return ret
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = countingSort(arr)
    print " ".join(map(str, result))


