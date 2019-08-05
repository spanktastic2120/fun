# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
s = ' '.join(input() for _ in range(n))
n = int(input())
for _ in range(n):
    w = input()
    p = re.compile('\\b('+w+')\\b')
    print(len(p.findall(s)))
