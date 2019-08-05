#!/bin/python

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    gw = len(G[0])
    gh = len(G)
    pw = len(P[0])
    ph = len(P)
    for r,row in enumerate(G[:gh - ph + 1]):
        for c in range(gw - pw + 1):
            if row[c:c+pw] == P[0][:]:
                # print "First row found"
                matched = True
                for pr, p in enumerate(P[1:]):
                    # print "searched row %s" % (pr + 2)
                    if p != G[r + pr + 1][c:c+pw]:
                        matched = False
                        break
                if matched:
                    return "YES"
                # print "not a match"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        RC = raw_input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in xrange(R):
            G_item = raw_input()
            G.append(G_item)

        rc = raw_input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in xrange(r):
            P_item = raw_input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
