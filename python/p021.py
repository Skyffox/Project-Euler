# pylint: disable=line-too-long
"""
Problem 21: Amicable Numbers

Problem description:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
"""

from utils import profiler


def sum_proper_divisors(n: int) -> int:
    """
    Returns the sum of proper divisors of a given integer n.

    Proper divisors of a number are all divisors of the number excluding the number itself.
    For example, the proper divisors of 28 are 1, 2, 4, 7, and 14, and their sum is 28.

    Args:
        n (int): The number for which to compute the sum of proper divisors.

    Returns:
        int: The sum of proper divisors of n.
    """
    divisors = [1]  # 1 is always a proper divisor
    for i in range(2, int(n ** 0.5) + 1):  # Iterate up to the square root of n
        if n % i == 0:  # i is a divisor
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice if it's a perfect square
                divisors.append(n // i)
    return sum(divisors)


@profiler
def compute() -> int:
    """
    Computes the sum of all amicable numbers under 10,000.

    Amicable numbers are two numbers where the sum of the proper divisors of each number 
    equals the other number. For example, 220 and 284 are amicable numbers because:
    - The sum of proper divisors of 220 is 284
    - The sum of proper divisors of 284 is 220

    This function finds all such pairs of amicable numbers below 10,000 and returns the 
    sum of all the amicable numbers.

    Returns:
        int: The sum of all amicable numbers under 10,000.
    """
    divisor_sums = {i: sum_proper_divisors(i) for i in range(2, 10000)}
    total = 0

    for a, b in divisor_sums.items():
        if b != a and b < 10000 and divisor_sums.get(b) == a:
            total += a

    return total


if __name__ == "__main__":
    print(f"Problem 21: {compute()}")
