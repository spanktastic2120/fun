#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

import string
width = len(word)
height = max([h[list(string.ascii_lowercase).index(c)] for c in word])
print width * height