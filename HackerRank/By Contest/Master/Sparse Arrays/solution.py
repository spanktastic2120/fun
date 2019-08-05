# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(sys.stdin.readline().strip())
strings = {}

for n in range(N):
    s = sys.stdin.readline().strip()
    if s in strings:
        strings[s] += 1
    else:
        strings[s] = 1

Q = int(sys.stdin.readline().strip())
for q in range(Q):
    s = sys.stdin.readline().strip()
    if s in strings:
        print strings[s]
    else:
        print 0