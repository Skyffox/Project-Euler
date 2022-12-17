#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 205.py:

import random

it = 0
max_it = 100000000
wins = 0

while it < max_it:
    peter = random.randrange(1, 5)
    colin = random.randrange(1, 7)

    if peter > colin:
        wins += 1

    it += 1

prob = wins / it
print("win percentage of peter %.7f" %prob)
