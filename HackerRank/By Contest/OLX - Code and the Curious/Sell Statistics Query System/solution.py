# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Sales():
    def __init__(self):
        self.records = [ [{},{},{},{},{},{},{},{},0] for _ in range(101) ]

    def add(self, d, p, c, s, r):

        if all([p,c,s,r]):
            key = tuple([p, c, s, r])
            if key in self.records[d][0]:
                self.records[d][0][key] += 1
            else:
                self.records[d][0][key] = 1

        if all([p,c,s]):
            key = tuple([p, c, s])
            if key in self.records[d][1]:
                self.records[d][1][key] += 1
            else:
                self.records[d][1][key] = 1

        if all([p,s,r]):
            key = tuple([p, s, r])
            if key in self.records[d][2]:
                self.records[d][2][key] += 1
            else:
                self.records[d][2][key] = 1

        if all([p,c]):
            key = tuple([p, c])
            if key in self.records[d][3]:
                self.records[d][3][key] += 1
            else:
                self.records[d][3][key] = 1

        if all([s,r]):
            key = tuple([s, r])
            if key in self.records[d][4]:
                self.records[d][4][key] += 1
            else:
                self.records[d][4][key] = 1


        if all([p,s]):
            key = tuple([p, s])
            if key in self.records[d][5]:
                self.records[d][5][key] += 1
            else:
                self.records[d][5][key] = 1

        if p:
            key = tuple([p])
            if key in self.records[d][6]:
                self.records[d][6][key] += 1
            else:
                self.records[d][6][key] = 1

        if s:
            key = tuple([s])
            if key in self.records[d][7]:
                self.records[d][7][key] += 1
            else:
                self.records[d][7][key] = 1

        self.records[d][8] += 1

    def lookup(self, d_s, d_e, p, c, s, r):
        d_e = d_s if not d_e else d_e
        count = 0

        for d in range(d_s, d_e + 1):
            if all([p,c,s,r]):
                key = tuple([p, c, s, r])
                count += self.records[d][0].get(key, 0)

            elif all([p,c,s]):
                key = tuple([p, c, s])
                count += self.records[d][1].get(key, 0)

            elif all([p,s,r]):
                key = tuple([p, s, r])
                count += self.records[d][2].get(key, 0)

            elif all([p,c]):
                key = tuple([p, c])
                count += self.records[d][3].get(key, 0)

            elif all([s,r]):
                key = tuple([s, r])
                count += self.records[d][4].get(key, 0)

            elif all([p,s]):
                key = tuple([p, s])
                count += self.records[d][5].get(key, 0)

            elif p:
                key = tuple([p])
                count += self.records[d][6].get(key, 0)

            elif s:
                key = tuple([s])
                count += self.records[d][7].get(key, 0)

            else:
                count += self.records[d][8]

        print count
        return

def parse(line):
    d, p, s = line[2:].split(' ')
    d = d.split('.')
    p = p.split('.')
    s = s.split('.')

    d_s = d_e = p_id = s_id = None
    c_id = r_id = 0
    if len(d) == 2:
        d_s, d_e = map(int, d)
    else:
        d_s = int(d[0])
        d = int(d[0])

    if len(p) == 2:
        p_id, c_id = map(int, p)
    else:
        p_id = int(p[0])

    if len(s) == 2:
        s_id, r_id = map(int, s)
    else:
        s_id = int(s[0])

    if p_id == -1:
        p_id = None
    if s_id == -1:
        s_id = None

    if line[0] == 'S':
        return tuple(['S', d, p_id, c_id, s_id, r_id])
    return tuple(['Q', d_s, d_e, p_id, c_id, s_id, r_id])
        
sales = Sales()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    line = sys.stdin.readline().strip()
    line = parse(line)
    if line[0] == 'S':
        sales.add(*line[1:])
    else:
        sales.lookup(*line[1:])
