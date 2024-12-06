ids, contents = [], []

with open('8.txt', 'r') as f:
    current_id = ""
    current_sequence = ""

    for line in f:
        line = line.strip()

        if line.startswith('>'):
            if current_id:
                ids.append(current_id)
                cnt = sum(1 for nucleotide in current_sequence if nucleotide in {'C', 'G'})
                contents.append(cnt / len(current_sequence))

            # Note that ids are only appended to the list after reading the whole corresponding sequence
            current_id = line[1:]
            current_sequence = ""
        else:
            current_sequence += line

    # Append the last sequence & its id
    if current_id:
        ids.append(current_id)
        cnt = sum(1 for nucleotide in current_sequence if nucleotide in {'C', 'G'})
        contents.append(cnt / len(current_sequence))

maxi, ind = 0, 0
for j, i in enumerate(contents):
    if i > maxi:
        maxi = i
        ind = j

print(ids[ind])
print(contents[ind] * 100)
