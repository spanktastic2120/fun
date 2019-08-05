#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = [a0, a1, a2]
    B = [b0, b1, b2]
    alice = 0
    bob = 0
    for a,b in zip(A,B):
        if (a > b):
            alice += 1
        elif (a < b):
            bob += 1
    return alice, bob

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))


