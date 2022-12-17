#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 72.py:
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000


def sieve_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    final = [1]
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            final.append(p)

    return final


total = 0
for d in range(2, 9):
    p = sieve_eratosthenes(d)

    total += len(p)

    print(p, d)


print("Total of reduced proper fractions", total)
