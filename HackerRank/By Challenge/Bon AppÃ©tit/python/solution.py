#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    anna = ar[0:k] + ar[k+1:]
    fair = sum(anna)/2
    if b == fair:
        return "Bon Appetit"
    return b - fair

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
