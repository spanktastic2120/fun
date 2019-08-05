#!/bin/python

import sys

def maximumGcdAndSum(A, B):
    N = 10**6
    countA = [0]*(10**6+1)
    countB = [0]*(10**6+1)
    for a in A:
        countA[a] += 1
    for b in B:
        countB[b] += 1
        
    mulA = [0]*(10**6+1)
    mulB = [0]*(10**6+1)
    for i in range(1,N+1):
        for j in range(i,N+1,i):
            if countA[j]:
                mulA[i] = j
            if countB[j]:
                mulB[i] = j

    for i in range(N-1,0,-1):
        if mulA[i] and mulB[i]:
            return mulA[i] + mulB[i]


if __name__ == "__main__":
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    res = maximumGcdAndSum(A, B)
    print res
