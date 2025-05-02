# pylint: disable=line-too-long
"""
Problem 72: Counting Fractions

Problem description:
This module solves the problem of finding the total number of reduced proper fractions for d ≤ 1,000,000.
A reduced proper fraction is a fraction in which the numerator and denominator are coprime (gcd(p, q) = 1).

Approach:
1. Use Euler's Totient Function (phi) to count the number of integers less than or equal to q that are coprime with q.
2. The function phi(q) gives the number of integers that are coprime with q for each q ≤ 1,000,000.
3. The total number of reduced proper fractions for denominators ≤ 1,000,000 is the sum of phi(q) for q in [2, 1,000,000].

Answer: 303963552391
"""

from itertools import islice
from typing import List
from utils import profiler


def list_totients(n: int) -> List[int]:
    """
    Compute the Euler's Totient Function for all integers from 1 to n.

    Args:
        n (int): The upper limit for the Euler's Totient Function.

    Returns:
        List[int]: A list where the i-th element is phi(i), the number of integers ≤ i that are coprime with i.
    """
    result = list(range(n + 1)) # Initialize the list with phi(i) = i for all i
    for i in range(2, len(result)):
        if result[i] == i: # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result


@profiler
def compute() -> str:
    """
    Compute the total number of reduced proper fractions for d ≤ 1,000,000.
    The total is the sum of Euler's Totient Function (phi(q)) for q from 2 to 1,000,000.

    Returns:
        str: The total number of reduced proper fractions for d ≤ 1,000,000.
    """
    totients = list_totients(10**6)
    ans = sum(islice(totients, 2, None))

    return str(ans)


if __name__ == "__main__":
    print(f"Problem 72: {compute()}")
