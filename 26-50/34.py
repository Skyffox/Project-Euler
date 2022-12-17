#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 34.py:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

sum = 0
for x in range(3, 100000):
    lst = list(str(x))
    tot = 0
    for num in lst:
        tot += factorial(int(num))

    if tot == x:
        sum += x
        
print ("Total for curious numbers:", sum)
