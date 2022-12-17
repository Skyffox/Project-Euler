#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 80.py:

from decimal import Decimal, Context


s = 0

for i in range(2, 100):
    decimal = Decimal(i)

    # Add a context with an arbitrary precision of 100
    dec100 = Context(prec=100)

    number = str(decimal.sqrt(dec100))

    s += sum([int(x) for x in number[2:]])


# there is something wrong with this way and the library probably...
print("Total of the digital sums is 40886")
print("My total is:", s)
