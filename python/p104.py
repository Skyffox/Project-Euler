# pylint: disable=line-too-long
"""
Problem 104: Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
Answer: 329468
Execution time: 11.8364s
"""

from math import log
from utils import profiler


def first_n_digits(num, n):
    """Return the first n characters"""
    return num // 10 ** (int(log(num, 10)) - n + 1)


@profiler
def compute():
    """
    Compute fibonacci numbers that need to be pandigital for both the first 10 and last 10 letters
    I calculate the first and last ten letters this way because I ran into the limit for converting integers into strings
    """
    fibnum_1 = 1
    fibnum_2 = 1
    fib = 0
    iterator = 2

    while True:
        iterator += 1
        fib = fibnum_1 + fibnum_2

        # Get last 9 characters
        tail = fib % 10**9
        if ''.join(sorted(str(tail))) == "123456789":
            # Get the first 9 characters
            head = first_n_digits(fib, 9)
            if ''.join(sorted(str(head))) == "123456789":
                return iterator

        fibnum_2 = fibnum_1
        fibnum_1 = fib

if __name__ == "__main__":
    print(f"Problem 104: {compute()}")
