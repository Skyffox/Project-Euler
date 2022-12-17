#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 71.py:


UPPER_BOUND = 1000000

top = 3
bot = 7

r = 0
s = 1

# if r/s < p/q then r*q = p*s and if we know that
# p/q < 3/7 then p = 3*q -1 / 7
for q in range(UPPER_BOUND, 0, -1):
    p = int((top*q - 1) / bot)

    if p * s > r * q:
        r = p
        s = q

print("Answer:", r, s)
