#!/bin/python

import sys

def buyMaximumProducts(n, k, a):
    # Complete this function
    b = sorted((e,i) for i,e in enumerate(a))
    stocks = 0
    for stock in b:

        price = stock[0]
        smax = stock[1] + 1
        
        if k < price:
            break

        buy = min(smax, k//price)
        k -= buy * price
        stocks += buy

    return stocks
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    k = long(raw_input().strip())
    result = buyMaximumProducts(n, k, arr)
    print result