# pylint: disable=line-too-long
"""
Problem 74: Digit Factorial Chains

Problem description:
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 145.

Consider a chain starting with a number below one million, where each successive number is the sum of the factorial of its digits.
For example:
    Starting with 69:
    69 → 363600 → 1454 → 145 → 42 → 6 → 720 → 5040 → 144 → 145
    The sum of factorials of the digits leads us back to 145, forming a chain.

The problem asks how many chains, starting with a number below one million, contain exactly 60 non-repeating terms.

Answer: 402
"""

import math
from utils import profiler


def sum_of_factorials(n: int, fac: list) -> int:
    """
    Computes the sum of the factorial of the digits of a number n.
    
    Args:
        n (int): The number to process.
        fac (list): Precomputed factorials for digits 0-9.
    
    Returns:
        int: The sum of the factorials of the digits of n.
    """
    return sum(fac[int(digit)] for digit in str(n))


@profiler
def compute() -> int:
    """
    Computes the number of chains, starting with a number below one million, 
    that contain exactly 60 non-repeating terms.
    
    Returns:
        int: The number of chains with exactly 60 non-repeating terms.
    """
    # Precompute factorials for digits 0-9
    fac = [math.factorial(i) for i in range(10)]

    # Initialize the result counter
    ans = 0

    # Iterate over all numbers below one million
    for i in range(2, 1000001):
        chain = []
        seen = set()
        s = i

        # Generate the chain and track the terms
        while s not in seen:
            seen.add(s)
            chain.append(s)
            s = sum_of_factorials(s, fac)

        # Check if the chain has exactly 60 non-repeating terms
        if len(chain) == 60:
            ans += 1

    return ans


if __name__ == "__main__":
    print(f"Problem 74: {compute()}")
