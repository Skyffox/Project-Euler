#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 32.py:
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.


def pandigital(multiplicand, multiplier, product):
    # dit kan vele malen sneller
    m1 = list(map(int, str(multiplicand)))
    m2 = list(map(int, str(multiplier)))
    m3 = list(map(int, str(product)))

    lst = m1 + m2 + m3
    
    # Numbers 1 through 9
    if sorted(lst) == list(range(1, 10)):
        return True
    return False
    

total_product = []

for i in range(1, 50):
    for j in range(1, 2000):
        product = i * j
        if pandigital(i, j, product):
            total_product.append(product)

print(sum(set(total_product)))
