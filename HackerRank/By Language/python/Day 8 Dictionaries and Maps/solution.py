# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
num = int(sys.stdin.readline())
phoneBook = {l:r for l, r in (sys.stdin.readline().strip().split(' ') for i in range(num))}
for line in sys.stdin.readlines():
    line = line.strip()
    if phoneBook.get(line):
        print line + '=' + phoneBook[line]
    else:
        print "Not found"