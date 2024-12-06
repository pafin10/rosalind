
totalWeight = 0
with open('21.txt', 'r') as f:
    s = ""
    for line in f:
        line = line.strip()
        s += line

aaWeights = {}
with open('../massTable.txt', 'r') as f1:
    for line in f1:
        cont = line.split()
        aa, weight = cont[0], cont[1]
        aaWeights[aa] = weight

for i in range(len(s)):
    totalWeight += float(aaWeights[s[i]])

print(round(totalWeight, 3))
