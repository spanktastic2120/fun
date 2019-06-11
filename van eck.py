seen = {}
pos = cur = nxt = 0
while True:
    print(cur, end=', ')
    nxt = pos - seen[cur] if cur in seen else 0
    seen[cur] = pos
    pos += 1
    cur = nxt
