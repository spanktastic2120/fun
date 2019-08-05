# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import sys
n = int(sys.stdin.readline().strip())
print n - Counter(map(int, sys.stdin.readline().strip().split(' '))).most_common(1)[0][1]