#!/bin/python

import sys

q = int(raw_input().strip())

for _ in range(q):
    n, m, library, road = map(int, raw_input().strip().split(' '))
    
    if library < road:
        print n * library
        for __ in xrange(m):
            raw_input()
        continue

    zones = []
    cities = {}
    zonecount = 0

    for __ in range(m):
        c1, c2 = raw_input().strip().split(' ')

        # cities are both new
        if c1 not in cities and c2 not in cities:

            # make a new zone for them
            zones.append(set((c1, c2)))

            # increment zone count
            zonecount += 1

            # update `cities` references
            cities[c1] = cities[c2] = len(zones) - 1

        # one city is new
        elif c1 not in cities or c2 not in cities:
            if c1 in cities:
                zones[cities[c1]].update( [c2] )
                cities[c2] = cities[c1]
            else:
                zones[cities[c2]].update( [c1] )
                cities[c1] = cities[c2]

        # cities are already connected
        elif cities[c1] == cities[c2]:
            continue

        # zones are merging
        else:
            delzone = cities[c2]

            # update `cities` reference for all cities in the
            # same zone as `c2`
            for c in zones[cities[c2]]:
                cities[c] = cities[c1]

            # add cities from c2's zone to c1's zone
            zones[cities[c1]].update(zones[delzone])
            zones[delzone] = None

            zonecount -= 1

    zonecount += n - len(cities)

    print (library * zonecount) + (road * (n - zonecount))