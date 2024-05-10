import requests
import re


def download_uniprot_sequence(accession_number):
    url = f"https://www.uniprot.org/uniprot/{accession_number}.fasta"
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        response.raise_for_status()


if __name__ == '__main__':
    id_seq, full_ids = {}, {}
    with open('finding_a_protein_motif.txt', 'r') as f:
        for line in f:
            full_id = line.strip()
            id = full_id.split('_')[0]
            full_ids[id] = full_id
            seq = download_uniprot_sequence(id).strip()
            seq_lines = seq.strip().split('\n')
            cleaned_seq = ''.join(seq_lines[1:])
            id_seq[id] = cleaned_seq.strip()

    pattern = re.compile(r'N(?=([^P]([ST])[^P]))')
    out_dict = {}
    for i, s in id_seq.items():
        matches = list(re.finditer(pattern, s))  # Convert iterator to list
        if matches:
            if i not in out_dict:
                out_dict[i] = []
            for p in matches:
                start_pos = p.start(1)  # Start position of the first capturing group
                out_dict[i].append('%02d' % start_pos)

    for k, v in out_dict.items():
        print(full_ids[k])
        for el in v:
            print(el, end="\t")
        print()
