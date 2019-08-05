import random

n = []
k = []
A = [[], [], [], [], []]
print "5"
for t in range(5):
    while 1:
        r = random.randint(3,200)
        if r not in n:
            n.append(r)
            break

    k.append(random.randint(1, n[t]))
    A[t].append(0)
    if t % 2 == 0:
        A[t] += [int(0 - random.randint(1,10**3)) for _ in range(1,k[t]-2)]
        A[t] += [random.randint(1,10**3) for _ in range(n[t]-k[t]+2)]
    else:
        A[t] += [int(0 - random.randint(1,10**3)) for _ in range(k[t]+1)]
        A[t] += [random.randint(1,10**3) for _ in range(k[t]+2,n[t])]

    print ' '.join(map(str, [n[t], k[t]]))
    print ' '.join(map(str, A[t]))
    #late = sum(1 for i in A[t] if i > 0)
    #max = int(n[t]-k[t])
    #print 'max late: %s' % max
    #print 'late students: %s' % late
    #print 'YES' if late >= max else 'NO'