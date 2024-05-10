import math

with open('29.txt', 'r') as f:
    nums = list(map(int, f.readline().split()))
n, N = nums[0], nums[1]

organisms = int(math.pow(2, n))
counterProb = 0

for i in range(N):
    # calculate binomial coefficient "organisms choose i"
    binom_coef = math.factorial(organisms) / (math.factorial(i) * math.factorial(organisms - i))
    # calculate binomial probability
    counterProb += binom_coef * math.pow(0.25, i) * math.pow(0.75, organisms - i)

print(1 - counterProb)
