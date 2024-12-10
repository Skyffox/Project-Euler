# How many n-digit positive integers exist which are also an nth power?
# Execution time: 0.316s

n_digit = 0
n = 1000

for x in range(1, n):
    for y in range(1, n):
        num = y**x
        l = len(list(str(num)))

        if l > x:
            break
        if l == x:
            n_digit += 1

print(n_digit)
