#!/bin/python

import sys

if __name__ == "__main__":
    n, m, k = map(int, raw_input().strip().split(' '))
    sockets = []
    for _ in xrange(m):
        x, y = map(int, raw_input().strip().split(' '))
        # left
        if not x:
            sockets.append(y)
        # bottom
        elif not y:
            sockets.append((4*n) - x)
        # right
        elif x == n:
            sockets.append((3*n) - y)
        # top
        else:
            sockets.append(n + x)
        #print sockets[-1]
            
    sockets = sorted(sockets)
    best = n*4

    # check contiguous sockets
    for i in xrange(m-k):
        if sockets[i+k-1] - sockets[i] < best:
            best = sockets[i+k-1] - sockets[i]
        if not best:
            break

    # check wrapped sockets
    if best:
        for i in xrange(k-1):
            if ((sockets[i] + (4 * n)) - sockets[i + 1 - k]) < best:
                best = (sockets[i] + (4 * n)) - sockets[i + 1 - k]
            if not best:
                break

    print best