# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
# Execution time: 1.141s

import itertools

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
    
def getTenfolds(num):
    th, num = num//1000, num%1000
    hu, num = num//100, num%100
    te, num = num//10, num%10
    si = num
    return sorted([th, hu, te, si])

def get_answer(primes):
    answer = []
    for i, x in enumerate(primes):
        for y in primes[i+1:]:
            d1 = y - x
            # Calculate what z should be
            z = y + d1
            if z > 10000:
                break
            if z in primes[i+1:]:
                xlst = getTenfolds(x)
                ylst = getTenfolds(y)
                zlst = getTenfolds(z)
                if xlst == ylst and ylst == zlst:
                    answer.append([x, y, z])
    return answer

primes = []
lst = list(range(1, 10))
# now take the cartesian product
product_lst = [p for p in itertools.product(lst, repeat=4)]
for sub_lst in product_lst:
    num = int(''.join(map(str, sub_lst)))
    if is_prime(num):
        primes.append(num)

print (get_answer(primes))
