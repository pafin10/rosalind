
with open('30.txt', 'r') as f:
    n = int(f.readline())

a, b, c = 1, 0, 0
for i in range(n):
    b = a
    a = c
    c = a+b

print(c)