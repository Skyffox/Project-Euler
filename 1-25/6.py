#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 6.py:
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def square_sum(n):
    count = 0
    for number in range(1, n+1):
        count += number
    return count**2


def sum_square(n):
    count2 = 0
    for number2 in range(1, n+1):
        count2 += number2**2
    return count2


def total(n):
    return square_sum(n) - sum_square(n)


print(total(100))
