#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 36.py:

def is_palindrome(n):
    return str(n) == str(n)[::-1]

potential = []
total = 0
for x in range(1, 1000000):
    if is_palindrome(x):
        potential.append(x)
        
for y in potential:
    binary_lst = list(bin(y))[2:]
    binary_n = int(''.join(binary_lst))
    if is_palindrome(binary_n):
        total += y
        
print ("Sum of double-base palindromes:", total)
    
