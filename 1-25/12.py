#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 12.py:
# The sequence of triangle numbers is generated by adding the natural numbers.
# What is the value of the first triangle number to have over five hundred divisors?


def num_divisors(n):
    divisors = 1
    count = 0
    
    if n % 2 == 0:
        n = n/2
    
    while n % 2 == 0:
        count += 1
        n = n/2
    
    divisors = divisors * (count + 1)
    p = 3
    
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n / p
        divisors = divisors * (count + 1)
        p += 2
    
    return divisors


def find_triangular_index():
    n = 1
    lnum = num_divisors(n)
    rnum = num_divisors(n + 1)
    while lnum * rnum < 500:
        n += 1
        lnum = rnum
        rnum = num_divisors(n+1)
    return n


index = find_triangular_index()
triangle = (index * (index + 1)) / 2
 
print(triangle)
