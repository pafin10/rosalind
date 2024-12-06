
with open('19.txt', 'r') as f:
    s = f.readline().strip()
    nums = f.readline().strip().split(" ")
    k, d = map(int, nums)

# TODO: THINK THROUGH LOGIC

def permutate(kmer, d):
    permutations = []
    charListkmer = list(kmer)
    mutations = {'A': ['T', 'C', 'G'], 'T': ['A', 'C', 'G'], 'C': ['A', 'T', 'G'], 'G': ['A', 'T', 'C']}
    for i in range(len(kmer)):
        for mutation in mutations[charListkmer[i]]:
            charListkmer[i] = mutation
            permutations.append(''.join(charListkmer))
            charListkmer[i] = kmer[i]
    if d == 2:
        for i in range(len(kmer)):
            for j in range(i+1, len(kmer)):
                for mutation1 in mutations[charListkmer[i]]:
                    for mutation2 in mutations[charListkmer[j]]:
                        charListkmer[i] = mutation1
                        charListkmer[j] = mutation2
                        permutations.append(''.join(charListkmer))
                        charListkmer[i] = kmer[i]
                        charListkmer[j] = kmer[j]
    elif d == 3:
        for i in range(len(kmer)):
            for j in range(i+1, len(kmer)):
                for k in range(j+1, len(kmer)):
                    for mutation1 in mutations[charListkmer[i]]:
                        for mutation2 in mutations[charListkmer[j]]:
                            for mutation3 in mutations[charListkmer[k]]:
                                charListkmer[i] = mutation1
                                charListkmer[j] = mutation2
                                charListkmer[k] = mutation3
                                permutations.append(''.join(charListkmer))
                                charListkmer[i] = kmer[i]
                                charListkmer[j] = kmer[j]
                                charListkmer[k] = kmer[k]
    return permutations

kmers = {}
for i in range(len(s) - k + 1):
    kmer = s[i:i+k]
    kmers[kmer] = kmers.get(kmer, 0) + 1
    permutations = permutate(kmer, d)
    for permutation in permutations:
        kmer = ''.join(permutation)
        kmers[kmer] = kmers.get(kmer, 0) + 1

kmersSorted = dict(sorted(kmers.items(), key=lambda item: item[1], reverse=True))
maxi = list(kmersSorted.values())[0]
out = []
for kmer, cnt in kmersSorted.items():
    if cnt == maxi:
        out.append(kmer)
    else:
        break

print(*out)