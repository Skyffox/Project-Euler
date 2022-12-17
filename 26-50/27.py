#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 27.py:
# Considering quadratics of the form: n2+an+b, where |a| < 1000 and |b| ≤ 1000
# Where |n| is the modulus/absolute value of n.
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.


def is_prime(num):
    if num <= 0:
        return False
    if num == 2:
        return True
    # Check if prime
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Count the number of primes
def check_primes(a, b):
    primes = 0
    for n in range(0, 1001):
        num = n**2 + n * a + b
        if is_prime(num):
            primes += 1
        else:
            break

    return primes


most_primes = 0
max_a = 0
max_b = 0

for a in range(-999, 1001):
    for b in range(-999, 1001):
        primes = check_primes(a, b)
        if primes > most_primes:
            most_primes = primes
            max_a = a
            max_b = b

product_coef = max_a * max_b
print ("Longest consecutive number of primes", most_primes)
print ("Most primes for a and b:", max_a, max_b)
print ("The largest product coefficient is:", product_coef)
