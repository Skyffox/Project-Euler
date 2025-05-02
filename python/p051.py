# pylint: disable=no-name-in-module, line-too-long
"""
Problem 51 - Prime Digit Replacements

Problem description:
This solution solves Problem 51, where the goal is to find the smallest prime number 
that can be transformed into a family of eight primes by replacing some of its digits 
with the same digit.

The number must be prime and, by replacing one or more of its digits with a single 
digit (0-9), a family of 8 prime numbers must be formed. The smallest prime number 
that satisfies this condition is the solution to the problem.

Answer: 121313
"""

from typing import Set, List
from utils import profiler, sieve_of_atkin


def generate_wildcard_patterns(s: str, index: int, searched: Set[str]) -> List[str]:
    """
    Generates all possible wildcard patterns for a given number by replacing digits 
    with a wildcard symbol (*) recursively. Each wildcard pattern is stored in the 
    returned list if it's unique.

    Args:
        s (str): The current number as a string.
        index (int): The index from which to start replacing digits with wildcards.
        searched (set): A set to track patterns that have already been searched.
    
    Returns:
        list: A list of wildcard patterns for the given string `s`.
    """
    wildcards = []
    if index > 0 and s not in searched:
        wildcards.append(s)
        searched.add(s)
    for x in range(index, len(s)):
        wildcards.extend(generate_wildcard_patterns(s[0:x] + '*' + s[x+1:], x+1, searched))
    return wildcards


@profiler
def compute() -> int:
    """
    Computes the smallest prime number that can be transformed into a family of eight primes 
    by replacing some of its digits with the same digit. The solution is based on generating 
    wildcard patterns for each prime and checking if the resulting numbers are prime.

    Returns:
        int: The smallest prime that satisfies the conditions of the problem.
    """
    # Generate all primes using the Sieve of Atkin up to 1 million
    primes = sieve_of_atkin(1000000)
    prime_set = set(primes)

    # Loop through all primes
    for prime in primes:
        searched = set() # Track searched wildcard patterns for this prime
        wildcards = generate_wildcard_patterns(str(prime), 0, searched)

        # Loop through all wildcard patterns
        for wildcard in wildcards:
            count = 0
            # Try replacing the wildcard (*) with digits from 0 to 9
            for digit in range(10):
                num = int(wildcard.replace('*', str(digit)))
                # Skip numbers with leading zeros
                if len(str(num)) < len(wildcard):
                    continue
                # Check if the number is prime
                if num in prime_set:
                    count += 1

            # If we have found at least 8 prime numbers, print the result and exit
            if count >= 8:
                return str(wildcard).replace("*", "1")

    return None


if __name__ == "__main__":
    print(f"Problem 51: {compute()}")
