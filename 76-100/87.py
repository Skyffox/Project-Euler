#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 87.py:

import math

def sieve_of_atkin(limit):
    P = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            P.append(p)
    return P


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
