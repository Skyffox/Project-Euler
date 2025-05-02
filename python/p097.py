# pylint: disable=line-too-long
"""
Problem 97: Large Non-Mersenne Prime

Problem description:
In 2004, a massive non-Mersenne prime was found with 2,357,207 digits: 28433 × 27830457 + 1.
The task is to find the last ten digits of this large prime number.

Answer: The last ten digits of the large prime number.
"""

from utils import profiler

@profiler
def compute():
    """Compute the last ten digits of the large non-Mersenne prime using modular arithmetic."""
    # Calculate the last ten digits of 28433 * 2^7830457 + 1
    return (28433 * pow(2, 7830457, 10000000000) + 1) % 10000000000

if __name__ == "__main__":
    print(f"Problem 97: {compute()}")
