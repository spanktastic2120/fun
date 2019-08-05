#!/bin/python

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    if n == 1:
        return grid
    grid = [[3 if e == "O" else 0 for e in c] for c in grid]
    initial = [list(g) for g in grid]
    filled = ["".join(["O" for e in c]) for c in grid]
    s1 = []
    s2 = []
    for i in range(1,6):
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == -1:
                    # exploded already
                    grid[r][c] = 0
                if col == 1:
                    # explode here
                    grid[r][c] = 0
                    if r+1 in range(len(grid)):
                        grid[r+1][c] = -1 if grid[r+1][c] != 1 else 1
                    if r-1 in range(len(grid)):
                        grid[r-1][c] = 0
                    if c+1 in range(len(row)):
                        grid[r][c+1] = -1 if grid[r][c+1] != 1 else 1
                    if c-1 in range(len(row)):
                        grid[r][c-1] = 0
                elif col > 1:
                    grid[r][c] -= 1
                elif i in [2,4] and col == 0:
                    grid[r][c] = 3
        if i == 3:
            s1 = [list(g) for g in grid]
        elif i == 5:
            s2 = [list(g) for g in grid]

    state = (n-1)%4
    if state == 2:
        grid = s1
    elif state == 0:
        grid = s2
    else:
        grid = filled
    
    for i,g in enumerate(grid):
        grid[i] = ''.join(["." if e == 0 else "O" for e in g])
    return grid
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = raw_input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in xrange(r):
        grid_item = raw_input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
