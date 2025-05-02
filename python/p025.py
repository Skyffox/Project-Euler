# pylint: disable=line-too-long
"""
Problem 25: 1000-digit Fibonacci Number

Problem description:
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

The Fibonacci sequence is defined by the recurrence relation:
    F₁ = 1, F₂ = 1
    Fₙ = Fₙ₋₁ + Fₙ₋₂

Find the index of the first term in the Fibonacci sequence to contain 1000 digits.

Answer: 4782
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Finds the index of the first Fibonacci number that contains at least 1000 digits.

    Returns:
        int: The index of the first Fibonacci number with at least 1000 digits.
    """
    a, b = 1, 1
    index = 2

    while len(str(b)) < 1000:
        a, b = b, a + b
        index += 1

    return index


if __name__ == "__main__":
    print(f"Problem 25: {compute()}")
