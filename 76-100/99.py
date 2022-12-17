#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 99.py:

import math

f = open("p099_base_exp.txt", "r")

best_line = 1
for it, line in enumerate(f):
    line = line.strip().split(",")
    line = [int(i) for i in line]

    if it == 0:
        n1 = line[1] * math.log(line[0])
        continue

    n2 = line[1] * math.log(line[0])

    if n2 > n1:
        n1 = n2
        best_line = it + 1

print(best_line)
