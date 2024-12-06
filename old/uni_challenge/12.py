seqs = []
with open('12.txt', 'r') as f:
    sequence = ''
    for line in f:
        if not line.startswith('>'):
            sequence += line.strip()
        elif sequence:
            seqs.append(sequence)
            sequence = ''
    seqs.append(sequence)

consMatrix = {'A': [], 'C': [], 'G': [], 'T': []}

ln = len(seqs[0])
for i in range(ln):
    cntA, cntC, cntG, cntT = 0, 0, 0, 0
    for j in range(len(seqs)):
        if seqs[j][i] == 'A':
            cntA += 1
        elif seqs[j][i] == 'C':
            cntC += 1
        elif seqs[j][i] == 'G':
            cntG += 1
        elif seqs[j][i] == 'T':
            cntT += 1
    consMatrix['A'].append(cntA)
    consMatrix['C'].append(cntC)
    consMatrix['G'].append(cntG)
    consMatrix['T'].append(cntT)

consensus = ''
for i in range(ln):
    maxi = 0
    for k, v in consMatrix.items():
        if v[i] > maxi:
            maxi = v[i]
            base = k
    consensus += base

print(consensus)
for k, v in consMatrix.items():
    print(k + ':', *v)
