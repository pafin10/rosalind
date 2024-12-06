with open('10.txt', 'r') as f:
    s = f.readline().strip()

aCnt, cCnt, gCnt, tCnt = 0, 0, 0, 0
for i in range(len(s)):
    if s[i] == 'A':
        aCnt += 1
    elif s[i] == 'C':
        cCnt += 1
    elif s[i] == 'G':
        gCnt += 1
    else :
        tCnt += 1

print(aCnt, cCnt, gCnt, tCnt)