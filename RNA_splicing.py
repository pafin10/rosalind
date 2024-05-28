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


def read_file():
    s, subs, start, sub = "", [], True, ""
    with open('RNA_splicing.txt', 'r') as f:
        f.readline()
        for line in f:
            if not line.startswith('>') and start:
                s += line.strip()
            elif line.startswith('>'):
                if sub:
                    subs.append(sub)
                sub = ""
                start = False
            else:
                sub += line.strip()
        if sub:
            subs.append(sub)
    return s, subs


def translate(s):
    i, protein = 0, ""
    while i < len(s) - 2:
        aa = codon_table[s[i:i + 3]]
        if not protein and aa != 'M':
            i += 1
        elif aa == 'M':
            protein += 'M'
            i += 3
        elif protein and not aa == '*':
            protein += aa
            i += 3
        elif aa == '*':
            break
    return protein


if __name__ == '__main__':
    # TODO: FIGURE OUT PROBLEM REALLY
    s, subs = read_file()
    print(s)
    print(*subs)

    repl = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    subs = [''.join(repl.get(c) for c in sub) for sub in subs]
    print(*subs)
    transcribed_s = ''.join(repl.get(c) for c in s)

    for sub in subs:
        ls = len(s)
        lk = len(sub)
        for i in range(ls - lk):
            if transcribed_s[i: i + lk] == sub:
                transcribed_s = transcribed_s.replace(sub, "")

    translated_s = translate(transcribed_s)
    print(translated_s)
