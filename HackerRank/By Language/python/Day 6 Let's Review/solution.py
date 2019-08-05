# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
num = int(sys.stdin.readline())
strings = [line.rstrip('\n') for line in sys.stdin.readlines()]
for i in range(num):
    print strings[i][0::2], strings[i][1::2]