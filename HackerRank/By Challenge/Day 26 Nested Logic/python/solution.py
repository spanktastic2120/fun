# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
rD, rM, rY = map(int, sys.stdin.readline().strip().split(' '))
eD, eM, eY = map(int, sys.stdin.readline().strip().split(' '))
if rY > eY:
    print "10000"
elif rM > eM and rY == eY:
    print "%s" % int(500*(rM-eM))
elif rD > eD and rM == eM and rY == rY:
    print "%s" % int(15*(rD-eD))
else:
    print "0"