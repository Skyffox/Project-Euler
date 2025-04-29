# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
# Execution time: 1.807s

from utils import sieve_of_atkin

BOUND = 50000000
LIMIT = int((BOUND - (2^3) - (2^4))**0.5)
primes = sieve_of_atkin(LIMIT)
total = 0
nums = []

for i in primes:
    if pow(i, 2) > BOUND:
        break
    for j in primes:
        if (pow(i, 2) + pow(j, 3)) > BOUND:
            break
        for k in primes:
            p = (pow(i, 2) + pow(j, 3) + pow(k, 4))
            if p > BOUND:
                break
            nums.append(p)

print(len(set(nums)))

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
