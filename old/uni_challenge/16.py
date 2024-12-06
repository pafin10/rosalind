
with open('16.txt', 'r') as f:
    txt = f.readline().strip()
    pattern = f.readline().strip()

lnP, lnT = len(pattern), len(txt)
cnt = 0
for i in range(lnT - lnP + 1):
    if txt[i: i+lnP] == pattern:
        cnt += 1

print(cnt)