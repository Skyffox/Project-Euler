#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 44.py:
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and
# D = |Pk − Pj| is minimised; what is the value of D?


def pentagonal(n):
    m = n * (3*n - 1) / 2
    if m == 151525092:
        print(n)
    return n * (3*n - 1) / 2


n = 10000
p_num = [int(pentagonal(z)) for z in range(1, n)]
# This way it is always lower.
D = p_num[-1]
b = False

print(p_num[-1])

for i, x in enumerate(p_num):
    for y in p_num[i+1:]:
        if x + y in p_num and y - x in p_num:
            D = abs(y - x)
            b = True
    if b:
        break

print(x, y, x+y)
                
print("Minimised difference:", D)


# getal*2 = 3n^2 - n

303050184
