# pylint: disable=line-too-long
"""
Problem 1: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
Answer: 31875000
Execution time: 0.0640s
"""

from utils import profiler


@profiler
def compute() -> int:
    """Find the first Pythagorean triplet till limit"""
    limit = 1000
    for c in range(0, limit):
        for b in range(0, c):
            a = limit - c - b
            if a**2 + b**2 == c**2:
                return a * b * c


if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
