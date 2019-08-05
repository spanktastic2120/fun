# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^[Hh][Ii]\s[^Dd]')
n = int(input())
for _ in range(n):
    m = input()
    if p.match(m): print(m)
