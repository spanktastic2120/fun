# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = re.compile('<([\w]+)([^>]*)>')
a = re.compile('\s([\w]+)=')
res = {}
n = int(input())
for _ in range(n):
    tags = t.findall(input())
    #print(tags)
    for tag in tags:
        attrs = a.findall(tag[1])
        if res.get(tag[0], None):
            attrs += res[tag[0]]
        res[tag[0]] = set(attrs)
        #print(tag, attrs)
#print(res)
for key in sorted(res.keys()):
    print(key + ':' + ','.join(sorted(res[key])))
