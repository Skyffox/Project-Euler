# Find the value of n ≤ 1,000,000 for which n/phi(n) is a maximum.
# Execution time: 0.215s

from helper import sieve_of_atkin

UPPER_BOUND = 1000000
sieve = sieve_of_atkin(100)
total = 1

# We know that the highest number for n/phi(n) is made up from only
# prime numbers, since those can only be divided by themselves.
for i in sieve:
    total *= i
    if total > UPPER_BOUND:
        print("Greatest value of n for which n/phi(n) is maximum:", total/i)
        break
