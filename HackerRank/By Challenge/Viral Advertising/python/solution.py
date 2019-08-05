# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(sys.stdin.readline().strip())
likes = 0
shares = 5
while n > 0:
    likes += int(shares/2)
    shares = 3 * int(shares/2)
    n -= 1
print likes