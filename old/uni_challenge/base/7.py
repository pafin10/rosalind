with open('7.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

cnt = 0
for i in range(len(s)):
    if s[i] != t[i]:
        cnt += 1

print(cnt)