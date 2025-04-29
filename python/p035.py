# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
# Execution time: 20.940s

from helper import sieve_of_atkin

primes = sieve_of_atkin(1000000)
tot_primes = 0

for p in primes[:len(primes)//2]:
    inv_p = int(str(p)[::-1])
    if inv_p in primes:
        tot_primes += 1

print("Total amount of circular primes:", tot_primes)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
