# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
# Execution time: ???

from helper import sieve_of_atkin

UPPER_BOUND = 10000000

sieve = sieve_of_atkin(10000)
total = 1

# We know that the highest number for n/phi(n) is made up from only
# prime numbers, since those can only be divided by themselves.
for i in sieve:
    total *= i
    if total > UPPER_BOUND:
        print("Greatest value of n for which n/phi(n) is maximum:", total/i)
        break
