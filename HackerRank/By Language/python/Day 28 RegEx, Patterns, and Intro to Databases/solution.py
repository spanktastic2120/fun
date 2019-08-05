#!/bin/python

import sys


N = int(raw_input().strip())
gmail = []
for _ in xrange(N):
    firstName,emailID = map(str, raw_input().strip().split(' '))
    if emailID.split('@')[1] in 'gmail.com':
        gmail.append(firstName)

gmail.sort()
print '\n'.join(g for g in gmail)