#!/bin/python

import sys
from collections import defaultdict

if __name__ == "__main__":
    n, q = map(int, raw_input().strip().split(' '))
    arr = map(int, raw_input().strip().split(' '))

    subarrs = (n * (n+1)) / 2 # constant
    indices = defaultdict(list)
    cache = defaultdict(int)

#    for i in range(n):
#        indices[arr[i]].append(i)
    [indices[val].append(i) for i, val in enumerate(arr)]

    for _ in xrange(q):
        x, y = map(int, raw_input().strip().split(' '))
        key = tuple([x, y if x < y else y, x])

        # lookup previous identical queries
        if cache[key]:
            print cache[key]
            continue

        else:
            xi, yi = indices[x], indices[y]
            xiLen, yiLen = len(xi), len(yi)
            
            if x == y or (not xi and not yi):
                cache[key] = subarrs
                print subarrs
                continue

            # zipper the indices of x and y in order
            merged = []
            i = j = 0
            append = merged.append
            while (i < xiLen and j < yiLen):
                if xi[i] < yi[j]:
                    append((xi[i], x))
                    i += 1
                else:
                    append((yi[j], y))
                    j += 1

            for r in range(i, xiLen):
                append((xi[r], x))

            for r in range(j, yiLen):
                append((yi[r], y))

            a = b = r = l = 0
            diffs = defaultdict(int)
            mLen = len(merged)
            
            # add diff for elements before any occurances of x or y
            if mLen >= 1:
                diffs[0] += merged[0][0] + 1

            # add diff for every occurance of x and y in order
            for k in range(mLen - 1):
                if merged[k][1] == x:
                    a += 1
                else:
                    b += 1
                diffs[a-b] += merged[k+1][0] - merged[k][0]

            # add diff for elements after all occurances of x and y
            if merged[-1][0] < n:
                if merged[-1][1] == x:
                    a += 1
                else:
                    b += 1
                diffs[a-b] += n - merged[-1][0]

            # do the math
            ans = sum(d*(d-1) for d in diffs.values())/2
            cache[key] = ans
            print ans

