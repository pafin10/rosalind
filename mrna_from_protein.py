mrnas = 1
mod = 1_000_000
with open('mrna_from_protein.txt', 'r') as f:
    s = ""
    for line in f:
        line = line.strip()
        s += line

codon_freqs = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'STOP': 3, 'C': 2, 'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,
               'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4, 'W': 1}

for aa in s:
    mrnas = (codon_freqs[aa] * mrnas) % mod

mrnas *= 3 % mod
print(mrnas % mod)
