
with open('5.txt', 'r') as file:
    txt = file.readline().strip()

dic = {}
for word in txt.split(' '):
    dic[word] = dic.get(word, 0) + 1

for (key, value) in dic.items():
    print(key, value)