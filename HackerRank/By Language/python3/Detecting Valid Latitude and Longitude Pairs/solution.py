# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^\([-+]?((90(\.0+)?)|([1-8][0-9](\.[0-9]+)?)|([0-9](\.[0-9]+)?)), [-+]?((180(\.0+)?)|(1[0-7][0-9](\.[0-9]+)?)|([1-9][0-9](\.[0-9]+)?)|([0-9](\.[0-9]+)?))\)$')

n = int(input())
for _ in range(n):
    if p.match(input()):
        print('Valid')
    else:
        print('Invalid')
