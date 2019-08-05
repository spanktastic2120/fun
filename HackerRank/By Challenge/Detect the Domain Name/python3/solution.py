# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('https?://(?:www.|ww\d.)?([a-zA-Z0-9-\.]+?\.[a-zA-Z0-9-\.]+)')
res = set()
n = int(input())
for _ in range(n):
    res.update(p.findall(input()))
print(';'.join(sorted(res)))
