# Find the sum of all the primes below two million.
# Execution time: 3.545s

from helper import sieve_of_atkin

print(sum(sieve_of_atkin(2000000)))
