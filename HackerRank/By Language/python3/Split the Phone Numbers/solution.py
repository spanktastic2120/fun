# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^([\d]{1,3})[\s-]([\d]{1,3})[\s-]([\d]{4,10})$')
n = int(input())
for _ in range(n):
    m = p.findall(input())
    print('CountryCode=%s,LocalAreaCode=%s,Number=%s' % m[0])
