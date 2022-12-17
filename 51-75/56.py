#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 56.py:

largest_s = 0
for a in range(101):
    for b in range(101):
        n = a**b
        lst = [int(x) for x in str(n)]
        s = sum(lst)
        
        if s > largest_s:
            largest_s = s

print (largest_s)
