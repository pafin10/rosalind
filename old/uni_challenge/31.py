with open('31.txt', 'r') as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))

cnt = 0
for i in range(n-1, -1, -1):
    currEl = a[i]
    k = i
    while k > 0:
        if a[i - k] > a[i]:
            cnt += 1
            #print("{} bigger than {}".format(a[i-k], a[i]))
        k -= 1
print(cnt)
