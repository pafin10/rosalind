with open('23.txt', 'r') as f:
    f.readline().strip()
    s = ""
    for line in f:
        line = line.strip()
        s += line

fourMers = {}
for i in range(len(s) - 4 + 1):
    fourMer = s[i:i+4]
    fourMers[fourMer] = fourMers.get(fourMer, 0) + 1

sorted4Mers = {k: fourMers[k] for k in sorted(fourMers.keys())}
for k, v in sorted(sorted4Mers.items()):
    print(v, end=' ')
