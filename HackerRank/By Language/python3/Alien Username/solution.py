# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^[_\.][0-9]+[a-zA-Z]*_?$')
n = input()
for _ in range(int(n)):
    print('VALID' if p.match(input()) else 'INVALID')
