# What is the least value of n for which the number of distinct solutions exceeds one-thousand?
# Execution time: ???

n = 180180 - 2
while True:
    solutions = 0

    for x in range(n, 10000000):
        for y in range(max(n, x), 10000000):
            if x + y == (x * y) / n:
                solutions += 1
                if solutions > 1000:
                    print(n)
                    break
    print(n)
    n += 1
