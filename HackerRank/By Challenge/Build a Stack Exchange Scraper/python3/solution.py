# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
p = re.compile('href=\"\/questions\/([0-9]+)\/.*?\>(.*?)\<\/a\>.*?\"relativetime\"\>(.*?)\<', re.DOTALL)
m = p.findall(sys.stdin.read())
for match in m:
    print(';'.join(match))
