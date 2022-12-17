#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 53.py:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def combinatorics(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
        
vals = 0
for n in range(1, 101):
    for r in range(n+1):
        if combinatorics(n, r) > 1000000:
            vals += 1
    
print (vals)
