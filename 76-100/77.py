#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 77.py:

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


n = 10
count = 0
primes = list(reversed(sieve_of_atkin(n)))

while len(primes) != 0:
    # if 10 % primes[0] == 0:
    #     count += 1

    n = 10
    for p in primes:
        while n > 0:
            n -= p
            if n == 0:
                count += 1
                break
            if n < 0:
                break
            print("first", n, p)
            for p2 in primes[1:]:
                if n % p2 == 0:
                    print("second", n, p2)
                    count += 1

    primes = primes[1:]

print(count)
