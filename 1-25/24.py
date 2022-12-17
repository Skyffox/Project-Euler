#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 24.py:
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of
# the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Gebruik itertools eindelijk sinds mooie functie voor permutations.
import itertools

x = itertools.permutations('0123456789', 10)
counter = 0
for i in x:
    counter += 1
    if counter == 1000000:
        print("".join(i))
        break
