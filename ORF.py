from collections import defaultdict
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',  # Phenylalanine (F) and Leucine (L)
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serine (S)
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',  # Tyrosine (Y) and Stop codons
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',  # Cysteine (C) and Tryptophan (W) and Stop codons
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Leucine (L)
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline (P)
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',  # Histidine (H) and Glutamine (Q)
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine (R)
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',  # Isoleucine (I) and Methionine (M, Start codon)
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine (T)
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',  # Asparagine (N) and Lysine (K)
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',  # Serine (S) and Arginine (R)
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valine (V)
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine (A)
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',  # Aspartic Acid (D) and Glutamic Acid (E)
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'  # Glycine (G)
}
def construct_rf(s):
    orfs, rf, orf_cnts, pos = [], "", defaultdict(bool), []
    for j in range(3):
        rf = ""
        i = j
        while i < len(s) - j - 4:
            if codon_table[s[i:i + 3]] != 'M' and not rf:
                i += 3
            if codon_table[s[i:i + 3]] == '*':
                if rf:
                    if not orf_cnts[rf]:
                        orfs.append(rf)
                    orf_cnts[rf] = True
                    rf = ""
            elif codon_table[s[i:i + 3]] == 'M' or rf:
                if codon_table[s[i:i + 3]] == 'M':
                    pos.append(i)
                rf += codon_table[s[i:i + 3]]
                i += 3
    return orfs, pos



if __name__ == '__main__':
    s = ""
    with open('ORF.txt', 'r') as f:
        f.readline()
        for line in f:
            s += line.strip()
    s = s.replace('T', 'U')
    orfs, pos = construct_rf(s)
    repl = {'A': 'U', 'G': 'C', 'C': 'G', 'U': 'A'}
    rev_s = s[::-1]

    reversed_replaced_s = ''.join(repl.get(c) for c in rev_s)
    rev_orfs, _ = construct_rf(reversed_replaced_s)
    orfs = orfs + rev_orfs

    for orf in orfs:
        first = True
        for i in range(len(orf)):
            if orf[i] == 'M':
                if not first:
                    orfs.append(orf[i:])
                first = False
    for o in set(orfs):
        if o:
            print(o)
