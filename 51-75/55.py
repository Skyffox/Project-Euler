#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 55.py:

def palindrome(num):
    return str(num) == str(num)[::-1]


lynchrel_nums = 0
for n in range(10000):
    is_palindrome = 0
    for it in range(51):
        reverse = int(str(n)[::-1])
        num = n + reverse
        if palindrome(num):
            is_palindrome = 1
            break
        n = num
    if is_palindrome == 0:
        lynchrel_nums += 1
    
print (lynchrel_nums)
