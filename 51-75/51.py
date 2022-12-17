#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 51.py:

import math


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


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
    return P, sieve


primes_lst, bool_sieve = sieve_of_atkin(125000)

# Go look if you can find more primes.
for num in primes_lst:
    num = str(num)

    for i in range(0, 10):
        c = 1
        i = str(i)
        if i not in num:
            continue

        for j in range(1, 10):
            j = str(j)
            if i == j:
                continue

            copy_num = num.replace(i, j)
            n = int(copy_num)

            if (n < 125000 and bool_sieve[n]) or is_prime(n):
                c += 1

            if c == 8:
                print("Smallest prime:", num)
                break
