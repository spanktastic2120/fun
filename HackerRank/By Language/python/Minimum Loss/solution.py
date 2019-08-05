# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
txt = sys.stdin.readlines()
years = int(txt[0])
prices = [int(p) for p in txt[1].split()]
minimum = None

indexed_prices = []

for i, p in enumerate(prices):
    indexed_prices.append((p,i))
    
indexed_prices.sort()
for n in range(1, years):
    if indexed_prices[n][1] - indexed_prices[n-1][1] < 0:
        if indexed_prices[n][0] - indexed_prices[n-1][0] < minimum or minimum is None:
            minimum = indexed_prices[n][0] - indexed_prices[n-1][0]



#for i, buy in enumerate(prices):
#    for sell in prices[i+1:]:
#        diff = buy - sell
#        if diff >= 0 and (diff < minimum or minimum is None):
#            minimum = diff

print minimum