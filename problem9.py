# pylint: disable=line-too-long
"""
Problem 1: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
Answer: 31875000
Execution time: 0.7907s
"""

from utils import profiler

@profiler
def find_pythagorean_triplet(limit: int) -> int:
    """Find the first Pythagorean triplet till limit"""
    for c in range(0, limit):
        for b in range(0, c):
            if b + c > limit:
                break
            for a in range(0, b):
                if a + b + c == limit and a**2 + b**2 == c**2:
                    return a * b * c


if __name__ == "__main__":
    print(f"Problem 1: {find_pythagorean_triplet(1000)}")
