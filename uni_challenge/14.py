seqs = []
with open('14.txt', 'r') as f:
    sequence = ""
    for line in f:
        line = line.strip()
        if not line.startswith('>'):
            sequence += line
        elif sequence:
            seqs.append(sequence)
            sequence = ""

seqs.append(sequence)
s1 = seqs[0]
s2 = seqs[1]


def transit(a, b):
    return (a == 'A' and b == 'G') or (a == 'G' and b == 'A') or (a == 'T' and b == 'C') or (a == 'C' and b == 'T')


def transv(a, b):
    return (a == 'G' and b == 'T') or (a == 'G' and b == 'C') or (a == 'T' and b == 'G') or (a == 'C' and b == 'G') or \
        (a == 'A' and b == 'T') or (a == 'A' and b == 'C') or (a == 'T' and b == 'A') or (a == 'C' and b == 'A')


ln = len(seqs[0])
cnt = 0
transitions, transversions = 0, 0
for i in range(ln):
    if not s1[i] == s2[i]:
        if transv(s1[i], s2[i]):
            transversions += 1
        elif transit(s1[i], s2[i]):
            transitions += 1

print(transitions / transversions)
