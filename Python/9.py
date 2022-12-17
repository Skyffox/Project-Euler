# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Execution time: 8.362s

def find_set(n):
    for c in range(0, n):
        for b in range(0, c):
            for a in range(0, b):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        return a * b * c

    return 0


print(find_set(1000))
