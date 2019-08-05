#!/bin/python

import sys


n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here
scores = sorted(list(set(scores)))
n = len(scores)   # number of scores to be searched
beaten = 0        # index of highest score in list that has been beating
high = int(n/2) # arbitrary score halfway through the list
for x in alice:
    if x < scores[beaten]:
        print n + 1
        continue

    broke = False
    while not broke:
        ###print beaten, high
        if x >= scores[high]:
            beaten = high
            if high + 1 == n:
                # higher than the highest score
                print 1
                broke = True
            elif x < scores[high+1]:
                print n - high
                broke = True
            elif x == scores[high+1]:
                print n - high - 1
                broke = True
            else:
                # raise the ceiling to halfway between n and high
                ###print "raising ceiling"
                high = int((n + high)/2)

        else:
            #lower the ceiling to halway between beaten and high
            ###print "lowering ceiling"
            high = int((beaten + high)/2)
            
            
            

