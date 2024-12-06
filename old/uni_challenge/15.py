
seqs = []
with open('15.txt', 'r') as f:
    sequence = ""
    for line in f:
        line = line.strip()
        if not line.startswith(">"):
            sequence += line
        elif sequence:
            seqs.append(sequence)
            sequence = ""

seqs.append(sequence)
s = seqs[0]
t = seqs[1]
pos = []
cnt = 0

for i in range(len(s)):
    if s[i] == t[cnt]:
        cnt += 1
        pos.append(i+1)
    if cnt == len(t):
        break
print(*pos)



