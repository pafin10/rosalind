
with open('26.txt', 'r') as f:
    nums = f.readline().strip().split()
    k, m, n = map(int, nums)

# k homo dominant, m hetero, n homo recessive
dom, rec = 0, 0
# mating with equal partner
dom += (k-1) * k / 2
rec += (n-1) * n / 2
dom += (m-1) * m / 2 * (3/4)
rec += (m-1) * m / 2 * (1/4)

# mating with different partner
dom += k*m
dom += k*n
dom += m*n/2
rec += m*n/2

print(dom/(dom+rec))