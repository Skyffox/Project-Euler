# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000
# Execution time: ???

from helper import sieve_of_atkin

total = 0
for d in range(2, 9):
    p = sieve_of_atkin(d)

    total += len(p)

    print(p, d)


print("Total of reduced proper fractions", total)
