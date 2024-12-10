# What is the first value which can be written as the sum of primes in over five thousand different ways?
# Execution time: ???

from helper import sieve_of_atkin

n = 10
count = 0
primes = list(reversed(sieve_of_atkin(n)))

while len(primes) != 0:
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
