#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 43.py:

import itertools as iter

pandigital_nums = [x for x in iter.permutations('0123456789')]
s = 0

for num in pandigital_nums:
    d = list(num)

    if int(''.join(d[1:4])) % 2 == 0 and int(''.join(d[2:5])) % 3 == 0 and int(''.join(d[3:6])) % 5 == 0 and \
       int(''.join(d[4:7])) % 7 == 0 and int(''.join(d[5:8])) % 11 == 0 and int(''.join(d[6:9])) % 13 == 0 and \
       int(''.join(d[7:10])) % 17 == 0:
        s += int(''.join(list(num)))

print(s)