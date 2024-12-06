
with open('6.txt', 'r') as file:
    txt = file.readline().strip()

rev = reversed(txt)
for base in rev:
    if base == 'T':
        print('A', end='')
    elif base == 'A':
        print('T', end='')
    elif base == 'G':
        print('C', end='')
    elif base == 'C':
        print('G', end='')
