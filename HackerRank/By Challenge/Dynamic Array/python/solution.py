# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N, Q = map(int, sys.stdin.readline().split(' '))
seqList = [[] for n in range(N)]
lastAnswer = 0
for q in range(Q):
    query, x, y = map(int, sys.stdin.readline().split(' '))
    
    if query == 1:
        seqList[(x^lastAnswer)%N].append(y)
    else:
        seq = seqList[(x^lastAnswer)%N]
        lastAnswer = seq[y%len(seq)]
        print lastAnswer