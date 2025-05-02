# pylint: disable=no-name-in-module, line-too-long
"""
Problem 60: Prime Pair Sets

Problem description:
This solution finds the smallest sum of a set of five primes such that every pair of primes 
in the set can concatenate to form another prime. The primes are selected such that, when concatenated 
in any direction, the resulting number must also be prime. The function finds the set of primes with 
the smallest sum that satisfies this condition.

Answer: 26033
"""

from utils import profiler, sieve_of_atkin, is_prime


def can_concatenate_primes(*primes: int) -> bool:
    """
    Check if concatenating a list of primes in all possible ways results in primes.
    
    Args:
        primes (int): A variable number of prime numbers.
    
    Returns:
        bool: True if all concatenations between primes are prime, otherwise False.
    """
    # Generate all pairwise concatenations of primes and check if they are prime
    for i, p1 in enumerate(primes):
        for j, p2 in enumerate(primes):
            if i != j:  # Skip concatenating a number with itself
                concatenation_1 = int(str(p1) + str(p2))
                concatenation_2 = int(str(p2) + str(p1))

                if not (is_prime(concatenation_1) and is_prime(concatenation_2)):
                    return False
    return True


@profiler
def compute() -> int:
    """
    This function generates a list of prime numbers using the Sieve of Atkin and then checks 
    for combinations of five primes that satisfy the condition that each pair of primes can concatenate 
    to form another prime number. The smallest sum of such a set is returned.

    Returns:
        int: The smallest sum of five primes that satisfy the problem condition.
    """
    # Set an upper limit for prime number generation
    primes = sieve_of_atkin(8500)

    # Iterate over all combinations of primes, considering the constraint of forming valid pairs
    for i, first in enumerate(primes[:-4]):
        for j, second in enumerate(primes[i+1:]):
            if can_concatenate_primes(first, second):
                for k, third in enumerate(primes[i+j+2:]):
                    if can_concatenate_primes(first, second, third):
                        for l, fourth in enumerate(primes[i+j+k+3:]):
                            if can_concatenate_primes(first, second, third, fourth):
                                for fifth in primes[i+j+k+l+4:]:
                                    if can_concatenate_primes(first, second, third, fourth, fifth):
                                        # Return the sum of the found primes
                                        return first + second + third + fourth + fifth
    return None


if __name__ == "__main__":
    print(f"Problem 60: {compute()}")
