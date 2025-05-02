# pylint: disable=line-too-long
"""
Problem 80: Square Root Digital Expansion

Problem Description:
We are asked to compute the total of the digital sums of the first 100 decimal digits 
of the square roots of non-perfect squares, for numbers from 2 to 100. The goal is to 
calculate the sum of these digits, excluding the perfect squares, since their square roots 
are integers. For each non-perfect square, we calculate its square root, extract the first 
100 decimal digits, and sum them. Finally, we compute the total sum of these individual sums.

Answer: 40886
"""

from decimal import Decimal, localcontext
from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the total sum of the digital sums of the square roots of the first 100 non-perfect squares.

    Returns:
        int: The total sum of the digital sums of the square roots of non-perfect squares.
    """
    total_sum = 0
    for x in range(1, 100):
        # Skip perfect squares as their square roots are integers and don't contribute to the sum
        if int(x**0.5) == x**0.5:
            continue

        # Use localcontext to set the precision for decimal operations
        with localcontext() as ctx:
            ctx.prec = 105 # We need 100 decimal digits plus a few extra for precision
            sqrt_x = Decimal(x).sqrt()

            # Convert the square root to a string and sum the first 100 decimal digits
            sqrt_str = str(sqrt_x)[2:101] # Extract the first 100 decimal digits (skip "1.")
            total_sum += sum(int(digit) for digit in sqrt_str) + int(str(Decimal(x).sqrt())[0])

    return total_sum


if __name__ == "__main__":
    print(f"Problem 80: {compute()}")
