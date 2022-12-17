#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 9.py:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def find_set(n):
    for c in range(0, n):
        for b in range(0, c):
            for a in range(0, b):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        return a * b * c

    return 0


print(find_set(1000))
