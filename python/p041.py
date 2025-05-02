# pylint: disable=no-name-in-module, line-too-long
"""
Problem 41: Pandigital Prime

Problem Description:
We are asked to find the largest n-digit pandigital prime. A pandigital number is one that 
uses all the digits from 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also a prime number.

We need to identify the largest pandigital prime by checking numbers with digits from 1 to n, 
where n <= 9, and checking if they are prime.

Answer: 7652413
"""

from itertools import permutations
from utils import profiler, is_prime


@profiler
def compute() -> int:
    """
    Finds the largest pandigital prime by generating permutations of the digits from 1 to n 
    (for n = 1 to 9), converting them into integers, and checking for primality.
    
    This function iterates over pandigital numbers with decreasing digits (starting from 9 digits),
    checking if each pandigital number is prime. The first prime encountered is returned.
    
    Returns:
        int: The largest pandigital prime.
    """
    # Iterate over n from 9 down to 1 (since we want the largest pandigital prime)
    for n in range(9, 0, -1):
        # Generate pandigital numbers using digits from 1 to n
        pandigital_digits = ''.join(map(str, range(1, n + 1)))

        # Generate permutations and check if any are prime
        for perm in sorted(permutations(pandigital_digits), reverse=True):
            num = int(''.join(perm))
            if is_prime(num): # Check if the number is prime
                return num # Return the largest pandigital prime found

    return None


if __name__ == "__main__":
    print(f"Problem 41: {compute()}")
