
with open('18.txt', 'r') as f:
    s = f.readline().strip()
    k = int(f.readline())

kmers = {}
for i in range(len(s) - k + 1):
    kmer = s[i:i+k]
    kmers[kmer] = kmers.get(kmer, 0) + 1

kmersSorted = dict(sorted(kmers.items(), key=lambda item: item[1], reverse=True))
maxi = list(kmersSorted.values())[0]
print(maxi)
out = []
for kmer, cnt in kmersSorted.items():
    if cnt == maxi:
        out.append(kmer)
    else:
        break

print(*out)