#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 16.py:
# What is the sum of the digits of the number 2^1000?


def power_digit_sum():
    print(sum([int(i) for i in str(2**1000)]))


power_digit_sum()
