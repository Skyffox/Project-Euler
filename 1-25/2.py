#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 2.py:
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.


def fibonacci_numbers(n):
    lst = [1, 2]
    first = 1
    second = 2
    third = first + second

    while third < n:
        lst.append(third)
        first, second = second, third
        third = first + second

    return lst


m_range = 4000000
total = 0

n = fibonacci_numbers(m_range)

print(sum([x for x in n if x % 2 == 0]))

