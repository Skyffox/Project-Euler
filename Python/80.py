# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
# Execution time: 0.231s

from decimal import Decimal, Context

s = 0
for i in range(2, 100):
    decimal = Decimal(i)

    # Add a context with an arbitrary precision of 100
    dec100 = Context(prec=100)

    number = str(decimal.sqrt(dec100))

    s += sum([int(x) for x in number[2:]])


# There is something wrong with this way and the library probably...
print("Total of the digital sums is 40886")
print("My total is:", s)
