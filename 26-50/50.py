#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 50.py:

# beter met een sieve
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    # Check only for odd numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
s = 0
n = 2
while True:
    if is_prime(n):
        s += n
        if s < 1000000:
            primes.append(n)
        else:
            break
    n += 1

len_pri = len(primes)
for x in range(len_pri):
    # Take x primes from the left
    l = primes[:-x]
    # Take x primes from the right
    r = primes[x:]
    
    if is_prime(sum(l)):
        longest_sum = sum(l)
        terms = len(l)
        break
        
    if is_prime(sum(r)):
        longest_sum = sum(r)
        terms = len(r)
        break

print (longest_sum, terms)
