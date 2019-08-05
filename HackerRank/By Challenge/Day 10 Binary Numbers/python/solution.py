#!/bin/python

import sys
from itertools import groupby

n = int(raw_input().strip())

print max([sum(1 for _ in r) for l, r in groupby(bin(n)[2:]) if l == '1'])
