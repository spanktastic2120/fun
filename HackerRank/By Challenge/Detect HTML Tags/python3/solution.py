# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('<(\w+)')
tags = set()
for _ in range(int(input())):
    tags.update(p.findall(input()))
print(';'.join(sorted(tags)))
