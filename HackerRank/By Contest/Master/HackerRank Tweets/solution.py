# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('hackerrank', re.IGNORECASE)
print(sum(1 if p.findall(input()) else 0 for _ in range(int(input()))))
