# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
# Execution time: 13.114s

import math

# return first n characters
def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

fib_1 = 1
fib_2 = 1
fib = 0
it = 2

# get last 9 characters
tailcut = 1000000000

while True:
    it += 1
    fib = fib_1 + fib_2

    tail = fib % tailcut
    taillst = list(str(tail))

    if sorted(taillst)  == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        digits = 1 + math.log10(fib)
        if digits > 9:
            head = first_n_digits(fib, 9)
            headlst = list(str(head))

            if sorted(headlst) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("First Fibonacci number with both pandigital:", it)
                break

    fib_2 = fib_1
    fib_1 = fib
