#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 48.py:

total = 0
for x in range(1, 1001):
    total += (x**x)

lst = list(str(total))
digits = lst[-10:]
ans = int(''.join(digits))
print (ans)
