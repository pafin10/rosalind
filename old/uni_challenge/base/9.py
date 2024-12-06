
with open('9.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

pos = []
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        pos.append(i + 1)

print(*pos)