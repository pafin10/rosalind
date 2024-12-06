import math
with open('28.txt', 'r') as f:
    s = f.readline().strip()
    probs = list(map(float, f.readline().strip().split()))

b = []
for prob in range(len(probs)):
    out = 0
    for i in range(len(s)):
        if s[i] == 'C' or s[i] == 'G':
            out += math.log(probs[prob]/2, 10)
        else:
            out += math.log((1-probs[prob])/2, 10)
    b.append(out)

print(*b)