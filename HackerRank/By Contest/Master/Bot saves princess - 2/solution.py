#!/bin/python
def nextMove(n,r,c,grid):
    prow = None
    pcolumn = None
    for pr, row in enumerate(grid):
        if "p" in row:
            prow = pr
            for pc, column in enumerate(row):
                if "p" in column:
                    pcolumn = pc

    if abs(prow - r) > abs(pcolumn - c):
        if prow - r > 0:
            return "DOWN"
        else:
            return "UP"
    elif pcolumn - c > 0:
        return "RIGHT"
    else:
        return "LEFT"


n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
