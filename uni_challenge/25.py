
with open('25.txt', 'r') as f:
    nums = f.readline().strip().split()
    n, m = map(int, nums)

youngsters = [1] + [0] * (n-1)
adults = [0] * n
for i in range(1, n):
    youngsters[i] = adults[i-1]
    adults[i] = adults[i-1] + youngsters[i-1] - youngsters[i-m]

print(adults[n-1] + youngsters[n-1])

