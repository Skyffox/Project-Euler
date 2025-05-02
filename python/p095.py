# pylint: disable=line-too-long
"""
Project Euler Problem 95: Amicable Chains

Problem description:
The problem seeks the smallest member of the longest amicable chain such that
no element in the chain exceeds one million. An amicable chain is formed by
repeatedly summing the proper divisors of a number until the sequence loops.

Answer: 14316
"""

import time
from utils import profiler

def sum_proper_divisors(n: int) -> int:
    """
    Returns the sum of proper divisors of a number n (excluding n itself).

    Args:
        n (int): The number for which to calculate the proper divisors.

    Returns:
        int: Sum of proper divisors of n.
    """
    if n < 2:
        return 0

    total = 1  # 1 is a proper divisor of every number > 1
    sqrt_n = int(n ** 0.5)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            complement = n // i
            if complement != i:
                total += complement

    return total


@profiler
def compute(limit: int = 1_000_000) -> int:
    """
    Computes the smallest member of the longest amicable chain under the given limit.

    Args:
        limit (int): Upper bound for values in the chain (default: 1,000,000).

    Returns:
        int: The smallest member of the longest amicable chain.
    """
    divisor_sum_cache = [0] * (limit + 1)
    for i in range(1, limit + 1):
        divisor_sum_cache[i] = sum_proper_divisors(i)

    longest_chain_length = 0
    smallest_member_of_longest_chain = None
    visited = [False] * (limit + 1)

    for start in range(2, limit):
        if visited[start]:
            continue

        chain = []
        seen = {}
        n = start

        while n <= limit and n not in seen:
            if visited[n]:
                break

            seen[n] = len(chain)
            chain.append(n)
            n = divisor_sum_cache[n]

        if n in seen:
            cycle_start = seen[n]
            cycle = chain[cycle_start:]
            if all(x <= limit for x in cycle):
                if len(cycle) > longest_chain_length:
                    longest_chain_length = len(cycle)
                    smallest_member_of_longest_chain = min(cycle)

        for x in chain:
            if x <= limit:
                visited[x] = True

    return smallest_member_of_longest_chain


if __name__ == "__main__":
    print(f"Problem 95: {compute()}")
