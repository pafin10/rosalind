with open('17.txt', 'r') as f:
    sub = f.readline().strip()
    s = ""
    for line in f:
        line = line.strip()
        s += line

pos = []
lnS, lnSub = len(s), len(sub)
for i in range(lnS-lnSub+1):
    if s[i:i+lnSub] == sub:
        pos.append(i)

print(*pos)