seqs = []
with open('20.txt', 'r') as f:
    k = int(f.readline())
    s = ""
    for line in f:
        line = line.strip()
        seqs.append(line)
ln = len(seqs[0])
kmers = []
for i in range(len(seqs)):
    for j in range(ln - k + 1):
        kmer = seqs[i][j: j+ k]
        kmers.append(kmer)

def hammingDist(seq, kmer, k):
    mini = 10E10
    for i in range(len(seq) - k + 1):
        dist = 0
        seqKmer = seq[i:i+k]
        for j in range(k):
            if seqKmer[j] != kmer[j]:
                dist += 1
        if dist < mini:
            mini = dist
    return mini


kmerDist = {}
for kmer in kmers:
    overall, d = 0, 0
    for seq in seqs:
        d += hammingDist(seq, kmer, k)
    overall += d
    kmerDist[kmer] = overall

sortedKmerDist = dict(sorted(kmerDist.items(), key=lambda it: it[1]))
print(list(sortedKmerDist)[0])
