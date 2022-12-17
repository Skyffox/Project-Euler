#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 47.py:
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

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


primes = sieve_of_atkin(1000)
consecutive = 0
solution = 0
ans = 4

for n in range(2, 150000):
    found = False
    distinct = 0

    if consecutive == 0:
        solution = n

    for p in primes:
        frac = n / p

        if frac < 1 or distinct > ans:
            consecutive = 0
            distinct = 0
            break

        if frac == int(frac):
            distinct += 1

            while n / p == int(n / p):
                n /= p

                if n == 1.0 and distinct == ans:
                    consecutive += 1
                    found = True

    if not found:
        consecutive = 0

    if consecutive == ans:
        break


print("First number of four consecutive integers with four distinct primes:", solution)
