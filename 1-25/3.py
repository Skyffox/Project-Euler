#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 3.py:
# What is the largest prime factor of the number 600851475143.
# A prime factor of a positive integer are prime numbers that divide that
# integer exactly.


def largest_prime_number():
    number = 600851475143
    i = 2

    while i * i < number:
        while number % i == 0:
            number /= i
        i += 1

    print(number)


largest_prime_number()
