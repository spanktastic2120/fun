# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('([\w\.]+@[\w\.]+\.[\w\.]+?[\w]+)')
n = int(input())
res = set()
for _ in range(n):
    res.update(p.findall(input()))
print(';'.join(sorted(res)))
