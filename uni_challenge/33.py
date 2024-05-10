
with open('../rosalind_ms.txt', 'r') as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))

A, B = a[:n // 2], a[n // 2:]
A.sort()
B.sort()
n, m = len(A), len(B)

start = min(A[0], B[0])
if start == A[0]:
    i, j = 1, 0
else:
    i, j = 0, 1
out = [start]

while i < n or j < m:
    # determine min, next of unused array, if all el of one have been used up
    if i < n and j < m:
        mini = min(A[i], B[j])
    elif i == n:
        mini = B[j]
    else:
        mini = A[i]
    # increase respective indices for next comparison
    if i < n and mini == A[i]:
        i += 1
    elif j < m and mini == B[j]:
        j += 1
    out.append(mini)

print(*out)
