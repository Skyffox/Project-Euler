#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 31.py:
# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

# Amount of money we have
total = 200
# All the possible combinations
s = [1,2,5,10,20,50,100,200]
# Amount of different currencies
siz = 8


# Return 1 when a combination can be made otherwise return 0
def count(total, s, size):
    if (total < 0):
        return 0
    if (total == 0):
        return 1
    if (size == 1):
        return 1
    else:
        # Go through each possible combination
        return count(total, s, size-1) + count(total-s[size-1], s, size)
    

print (count(total, s, siz))

