# pylint: disable=line-too-long
"""
Problem 73: Counting Fractions in a Range

Problem description:
Consider the fraction a/b, where a and b are positive integers.
We want to count how many fractions a/b, where 1 < a < b and gcd(a, b) = 1,
lie between 1/3 and 1/2 (exclusive), and the denominator b is less than or equal to a given limit.

For a fraction a/b to lie between 1/3 and 1/2, it must satisfy:
    1/3 < a/b < 1/2
    Additionally, the fraction must be in its simplest form, meaning gcd(a, b) = 1.

Answer: 7295372
"""

import math
from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the number of fractions between 1/3 and 1/2 with denominator <= 12,000.
    
    Returns:
        int: The result for the given limit.
    """
    limit = 12000
    count = 0

    for b in range(2, limit + 1):
        # Find the range for a (where a/b is between 1/3 and 1/2)
        lower_bound = b // 3 + 1
        upper_bound = b // 2
        # Count the numbers a in this range where gcd(a, b) = 1
        for a in range(lower_bound, upper_bound + 1):
            if math.gcd(a, b) == 1:
                count += 1
    return count - 1


if __name__ == "__main__":
    print(f"Problem 73: {compute()}")
