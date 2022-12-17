#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 63.py:
# How many n-digit positive integers exist which are also an nth power?

n_digit = 0
n = 1000

for x in range(1, n):
    for y in range(1, n):
        num = y**x
        l = len(list(str(num)))

        if l > x:
            break
        if l == x:
            n_digit += 1

print(n_digit)
