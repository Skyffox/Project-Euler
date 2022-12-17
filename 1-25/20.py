#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 20.py:
# Find the sum of the digits in the number 100!


def equation(inputs):
    counter = 1
    for number in range(1, inputs + 1):
        counter *= number
    return counter


def sumOfEquation():
    indivNumbers = [int(i) for i in str(equation(100))]
    return sum(indivNumbers)


numSum = sumOfEquation()
print ("The sum of the digits in the number 100! ", str(numSum))
