# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^[A-Z]{5}[0-9]{4}[A-Z]$')
n = int(input())
for _ in range(n):
    print('YES' if p.findall(input()) else 'NO')
