def read_fasta(fastafile):
    ids = []
    sequences = []
    sequence = ""

    with open(fastafile, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                id = line[1:]
                ids.append(id)

                if sequence:
                    sequences.append(sequence)
                    sequence = ""

            else:
                sequence += line

        # append last sequence
        if sequence:
            sequences.append(sequence)

    return sequences


def find_longest_substring(sequences):
    longest_substring = ""
    substring = ""

    for i in range(len(sequences[0])):
        for j in range(len(sequences[0]) + 1):
            substring = sequences[0][i:j]
            present_in_all = all(substring in seq for seq in sequences[1:])

            if present_in_all and len(substring) > len(longest_substring):
                longest_substring = substring

    return longest_substring


if __name__ == '__main__':
    file = read_fasta("very_old/txt_files/rosalind_lcsm.txt")
    print(find_longest_substring(file))
