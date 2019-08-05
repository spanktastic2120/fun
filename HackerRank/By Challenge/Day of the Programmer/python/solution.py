#!/bin/python

import sys

def solve(year):
    # Complete this function
    if year >= 1919:
        leap = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
        return '.'.join([str(13 - leap), '09', str(year)])
    elif year <= 1917:
        leap = year % 4 == 0
        return '.'.join([str(13 - leap), '09', str(year)])
    else:
        leap = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
        return '.'.join([str(26 - leap), '09', str(year)])

year = int(raw_input().strip())
result = solve(year)
print(result)
