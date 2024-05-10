
with open('11.txt', 'r') as f:
    _ = f.readline().strip()
    s = ""
    for line in f:
        line = line.strip()
        s += line

def compl(seq):
    comp = ''
    for base in seq:
        if base == 'T':
            comp += 'A'
        elif base == 'A':
            comp += 'T'
        elif base == 'G':
            comp += 'C'
        elif base == 'C':
            comp += 'G'
    return comp


revPals = {}
wind = 4
ln = len(s)

while wind <= 12:
    for i in range(ln - wind + 1):
        sect = s[i:i + wind]
        complement = compl(sect)
        revComp = complement[::-1]
        if sect == revComp:
            revPals[i + 1] = wind
    wind += 1

for k, v in revPals.items():
    print(k, v)
