# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def readinput():
    n = int(input())
    lines = []
    for i in range(n):
        lines.append(input())
    t = int(input())
    tests = []
    for i in range(t):
        tests.append(input())
    return lines, tests

lines, tests = readinput()
words = '\n'.join(lines)
for t in tests:
    t = t.replace('our','o[u]?r')
    t = '\\b(' + t + ')\\b'
    print(len(re.findall(t, words)))
