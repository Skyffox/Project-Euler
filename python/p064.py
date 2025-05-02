# pylint: disable=line-too-long
"""
Problem 64: Odd Period Square Roots

Problem description:
This module solves the problem of counting how many continued fractions for square roots of numbers 
up to a given limit have an odd period.

Answer: 1322
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes how many continued fractions for square roots of N ≤ 10000 have an odd period.

    Returns:
        int: The number of continued fractions with odd periods for N ≤ 10000.
    """
    odd_periods = 0

    for root in range(2, 10000):
        m_n = 0
        d_n = 1
        a0 = int(root ** 0.5)

        # Skip perfect squares
        if a0 * a0 == root:
            continue

        a_n = a0
        triplets = []
        period = []

        # Generate continued fraction expansion
        while True:
            m_n = d_n * a_n - m_n
            d_n = (root - m_n ** 2) // d_n  # Integer division
            a_n = (a0 + m_n) // d_n  # Integer division

            # Check for repetition of triplets, indicating the start of the period
            if [m_n, d_n, a_n] in triplets:
                break

            triplets.append([m_n, d_n, a_n])
            period.append(a_n)

        # Count if the period length is odd
        if len(period) % 2 != 0:
            odd_periods += 1

    return odd_periods


if __name__ == "__main__":
    print(f"Problem 64: {compute()}")
