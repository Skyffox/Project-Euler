# pylint: disable=no-name-in-module, line-too-long
"""
Problem: Consecutive Prime Sum

Problem Description:
We are tasked with finding the prime below one million that can be written as 
the sum of the most consecutive primes. The prime numbers are summed in consecutive 
order, and the goal is to determine which prime, below one million, can be expressed 
as the sum of the largest number of consecutive primes.

Answer: 997651
"""

from utils import profiler, is_prime


@profiler
def compute() -> int:
    """
    Finds the prime below one-million that can be written as the sum of the most consecutive primes.
    
    This function generates a list of primes below one million and checks the sums 
    of consecutive primes to determine which prime can be written as the sum of 
    the most consecutive primes.
    
    Returns:
        int: The prime that is the sum of the most consecutive primes and the number of terms.
    """
    primes = []
    s = 0
    n = 2
    while True:
        if is_prime(n):
            s += n
            if s < 1000000:
                primes.append(n)
            else:
                break
        n += 1

    len_pri = len(primes)
    longest_sum = 0

    # Iterate through the list of primes and check sums of consecutive primes
    for x in range(len_pri):
        l = primes[:-x] # Take x primes from the left
        r = primes[x:] # Take x primes from the right

        if is_prime(sum(l)):
            longest_sum = sum(l)
            break

        if is_prime(sum(r)):
            longest_sum = sum(r)
            break

    return longest_sum


if __name__ == "__main__":
    print(f"Problem 50: {compute()}")
