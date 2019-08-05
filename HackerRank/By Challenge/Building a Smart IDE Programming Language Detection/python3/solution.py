# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
java = re.compile('^[\s]*import java', re.MULTILINE)
c = re.compile('^[\s]*#include', re.MULTILINE)
i = sys.stdin.read()
print('Java' if java.findall(i) else 'C' if c.findall(i) else 'Python')
