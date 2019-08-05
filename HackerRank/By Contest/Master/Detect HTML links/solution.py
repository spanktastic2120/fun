# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('<a href="(.*?)".*?>([^<>]*?)</')
n = int(raw_input())
for _ in range(n):
    matches = p.finditer(raw_input())
    for m in matches:
        print "%s,%s" % (m.group(1).strip(), m.group(2).strip())
