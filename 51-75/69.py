#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 69.py:
# Find the value of n ≤ 1,000,000 for which n/phi(n) is a maximum.

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
