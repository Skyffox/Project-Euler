#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 33.py:

# Find the common divisor of a numerator and denominator.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Simplify the four non-trivial fractions and calculate the simplified
# denominator afterward for the answer.
def simplify(lst):
    super_num = 1
    super_den = 1
    
    for frac in lst:
        a = frac[0]
        b = frac[1]
        
        # Calculate the common divisor
        common_div = gcd(a, b)
        reduced_num = a / common_div
        reduced_den = b / common_div
        
        super_num *= reduced_num
        super_den *= reduced_den
        
    product_denom = gcd(super_num, super_den)
    denom = super_den / product_denom
    
    return denom


combinations = []
# Simulating the numerator and denominator
for x in range(10, 100):
    for y in range(10, 100):
        if x >= y:
            continue

        numerators = list(str(x))
        denominators = list(str(y))
        
        num1 = int(numerators[0])
        num2 = int(numerators[1])
        
        denom1 = int(denominators[0])
        denom2 = int(denominators[1])
        
        if num2 == denom1 and denom2 > 0 and x/y == num1/denom2:
            combinations.append([num1, denom2])

product_denom = simplify(combinations)

print (product_denom)
