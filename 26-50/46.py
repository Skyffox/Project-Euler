#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 46.py:

def eratosthenes(n):
    multiples = []
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
                
    return primes

import math
n = 6000
prime = eratosthenes(n)

for x in range(3, n, 2):
    for i, p in enumerate(prime):
        if p > x:
            break
            
        a = math.sqrt((x - p) / 2)
        if a.is_integer():
            break
    
    if not float(a).is_integer():
        print ("found answer", x, a)
