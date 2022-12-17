#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 5.py:
# What is the smallest positive number that is divisible by all of the number
# from 1 to 20.


def smallest_multiple():
    for number in range(20, 1000000000, 20):
        for iterator in range(1, 20):
            if number % iterator != 0:
                break

        if number % iterator == 0 and iterator == 19:
            print(number)
            break


smallest_multiple()
