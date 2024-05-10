
with open('27.txt', 'r') as f:
    nums = f.readline().strip().split()
    a, b, c, d, e, f = map(int, nums)

dom = (2*a + 2*b +2*c + 1.5*d + e)
print(dom)