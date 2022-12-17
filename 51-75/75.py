#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 75.py:

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


BOUND = 1500000
LIMIT = int((BOUND / 2)**0.5) # performance increase!
triangles = [0 for _ in range(BOUND + 1 )]
result = 0

for m in range(2, LIMIT):
    for n in range(1, m):
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            p = a+b+c
            while (p <= 1500000):
                if triangles[p] == 0:
                    triangles[p] = 1
                    result += 1
                elif triangles[p] == 1:
                    triangles[p] = 2
                    result -= 1

                p += a+b+c

print("Triangles with a right angle:", result)
