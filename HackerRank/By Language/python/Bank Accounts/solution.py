#!/bin/python

import sys

def feeOrUpfront(n, k, x, d, p):
    # Complete this function
    fee = sum(max(k, float(x)*pmt/100) for pmt in p)
    if d < fee:
        return 'upfront'
    return 'fee'

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, k, x, d = raw_input().strip().split(' ')
        n, k, x, d = [int(n), int(k), int(x), int(d)]
        p = map(int, raw_input().strip().split(' '))
        result = feeOrUpfront(n, k, x, d, p)
        print result

