def read_fasta(fasta_file):
    ids_ = []
    sequences_ = []
    current_sequence = ""

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()

            # extract ID
            if line.startswith(">"):
                sequence_id = line[1:]
                ids_.append(sequence_id)

                if current_sequence:
                    sequences_.append(current_sequence)
                    current_sequence = ""

            # append current line to sequence
            else:
                current_sequence += line

        # add the last sequence to the sequences list
        if current_sequence:
            sequences_.append(current_sequence)

    return ids_, sequences_


def compare_sequences(idss, sequencess):
    adjacency_strings = ""
    adjacency_dictionary = {}

    for key in idss:
        adjacency_dictionary[key] = []

    for i in range(len(sequencess)):
        for j in range(len(sequencess)):
            if i != j:
                if idss[i] in adjacency_dictionary:
                    if sequencess[i][-3:] == sequencess[j][:3]:
                        adjacency_dictionary[idss[i]].append(idss[j])

    adjacency_list = []
    for key, values in adjacency_dictionary.items():
        if values:
            for value in values:
                adjacency_list.append((key, value))

    return adjacency_list


if __name__ == '__main__':
    ids, sequences = read_fasta('/Users/mad_hatter/PycharmProjects/rosalind/src/txt_files/rosalind_grph.txt')

    adjacency_list = compare_sequences(ids, sequences)

    for entry in adjacency_list:
        print(entry[0], entry[1])
