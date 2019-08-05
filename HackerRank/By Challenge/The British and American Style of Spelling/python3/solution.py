# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
t = int(input())
for _ in range(t):
    american = input()
    british = american[0:-2] + 'se'
    p = re.compile('(%s|%s)' % (american, british))
    print(sum(len(p.findall(line)) for line in lines))
