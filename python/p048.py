# pylint: disable=line-too-long
"""
Problem 48: Self Powers

Problem Description:
We are tasked with finding the last ten digits of the series:

    1^1 + 2^2 + 3^3 + ... + 1000^1000.

The sum of this series grows very large, and we need to find the last ten digits of the result.

Answer: 9110846700
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the sum of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000 and returns the last 10 digits of the sum.
    
    Returns:
        int: The last ten digits of the computed sum.
    """
    total = 0
    # Iterate through numbers from 1 to 1000
    for x in range(1, 1001):
        total += (x**x)

    # Convert the total to a string, and extract the last ten digits
    lst = list(str(total))
    digits = lst[-10:]

    # Combine the last ten digits into an integer
    return int(''.join(digits))


if __name__ == "__main__":
    print(f"Problem 48: {compute()}")
