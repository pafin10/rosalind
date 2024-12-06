with open('32.txt', 'r') as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))
    m = int(f.readline().strip())
    b = list(map(int, f.readline().split()))

start = min(a[0], b[0])
if start == a[0]:
    i, j = 1, 0
else:
    i, j = 0, 1
out = [start]

while i < n or j < m:
    # determine min, next of unused array, if all el of one have been used up
    if i < n and j < m:
        mini = min(a[i], b[j])
    elif i == n:
        mini = b[j]
    else:
        mini = a[i]
    # increase respective indices for next comparison
    if i < n and mini == a[i]:
        i += 1
    elif j < m and mini == b[j]:
        j += 1
    out.append(mini)

print(*out)
