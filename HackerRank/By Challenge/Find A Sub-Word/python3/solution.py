# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
sen = []
for _ in range(int(input())):
    sen.append(input())

s = ' '.join(sen)

for _ in range(int(input())):
    n = input()
    p = re.compile('\w(' + n + ')\w')
    print(len(p.findall(s)))
