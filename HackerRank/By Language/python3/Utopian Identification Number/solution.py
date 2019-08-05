# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$')
n = int(input())
for _ in range(n):
    print('VALID' if p.findall(input()) else 'INVALID')
