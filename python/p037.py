# pylint: disable=no-name-in-module, line-too-long
"""
Problem 37: Truncatable Primes

Problem Description:
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

Answer: 748317
"""

from utils import profiler, is_prime


@profiler
def compute() -> int:
    """
    Computes the sum of the eleven primes that are truncatable from both left to right and right to left.
    
    This function checks for truncatable primes by iterating over numbers and testing if removing digits from both ends of the 
    number results in prime numbers at each stage.
    
    Returns:
        int: The sum of the eleven truncatable primes.
    """
    primes = 0
    sum_primes = 0
    n = 8 # Start from 8, as single-digit primes are not truncatable

    while primes < 11:
        if not is_prime(n): # Skip non-prime numbers
            n += 1
            continue

        lst = list(str(n)) # Convert the number to a list of characters

        # Generate truncations from the left
        left_truncations = [int(''.join(lst[x:])) for x in range(1, len(lst))]
        # Generate truncations from the right
        right_truncations = [int(''.join(lst[:-x])) for x in range(1, len(lst))]

        # Check if all truncations (both left and right) are prime
        if all(is_prime(num) for num in left_truncations) and all(is_prime(num) for num in right_truncations):
            primes += 1
            sum_primes += n

        n += 1

    return sum_primes


if __name__ == "__main__":
    print(f"Problem 37: {compute()}")
