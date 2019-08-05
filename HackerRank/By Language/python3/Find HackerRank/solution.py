# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p1 = re.compile('^hackerrank')
p2 = re.compile('hackerrank$')
n = int(input())
for _ in range(n):
    m = input()
    print('0' if p1.findall(m) and p2.findall(m) else '1' if p1.findall(m) else '2' if p2.findall(m) else '-1')
