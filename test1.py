# Find all prime numbers between 1 and N

print('hello from test1.py')

n = 10000
prime_nums = []

for i in range(1, n + 1):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c == 1:
        prime_nums.append(i)


print(prime_nums)
