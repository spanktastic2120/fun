# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(sys.stdin.readline().strip())
candidates = map(int, [sys.stdin.readline().strip() for _ in range(n)])

for c in candidates:
    if all([c != 2, c % 2 == 0]) or c == 1:
        print "Not prime"
        continue
    sc = int(c**0.5)
    prime = True
    for i in range(3, sc+2, 2):
        if c % i == 0:
            print "Not prime"
            prime = False
            break
    if prime:
        print "Prime"