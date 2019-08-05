# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
p = re.compile('(//.*?(?:\n)|/\*.*?\*/)', re.DOTALL)
lines = sys.stdin.read()
for m in p.findall(lines):
    for n in m.strip().split('\n'):
        print(n.strip())
