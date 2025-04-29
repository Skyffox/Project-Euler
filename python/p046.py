# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# It turns out that the conjecture was false. What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# Execution time: 0.462s

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

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
