#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 14.py:
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Although it has not been proved yet (Collatz Problem), it is thought that
# all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?


def collatz_sequence():
    long_chain = 0
    start_num = 0

    for n in range(2, 1000000):
        seq = n
        chain = 1
        while n != 1 or n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = n * 3 + 1

            chain += 1

        if chain > long_chain:
            long_chain = chain
            start_num = seq

    return start_num, long_chain


num, seq = collatz_sequence()
print("The starting number %d produces a sequence of %d." % (num, seq))


