# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
v4 = re.compile('^(([01]?\d?\d|2[0-4]?\d?|25[0-5])\.){3}([01]?\d?\d|2[0-4]?\d?|25[0-5])$')
v6 = re.compile('^[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}$')
for _ in range(int(input())):
    line = input()
    if v4.findall(line):
        print('IPv4')
    elif v6.findall(line):
        print('IPv6')
    else:
        print('Neither')
