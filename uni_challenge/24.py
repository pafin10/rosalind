
with open('24.txt', 'r') as f:
    nums = f.readline().strip().split()
    n, k = map(int, nums)

cnt, a, b = 1, 0, 1
while cnt < n:
    c = b + k * a
    a = b
    b = c
    cnt += 1

print(c)
