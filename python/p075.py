# pylint: disable=line-too-long
"""
Problem 75: Singular Integer Right Triangles

Problem description:
Consider a right-angled triangle where the lengths of the sides are integers.
Let the perimeter of the triangle be the sum of the three sides (a + b + c).
For a given perimeter value, L, we want to know how many right-angled triangles with integer sides can be formed.
For this problem, we are specifically interested in finding the number of values of L ≤ 1,500,000 such that exactly one unique right-angled triangle can be formed.

Answer: 161667
"""

from utils import profiler


def gcd(a: int, b: int) -> int:
    """
    Computes the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


@profiler
def compute() -> int:
    """
    Computes the number of values of L ≤ 1,500,000 for which exactly one integer-sided right angle triangle can be formed.
    
    Returns:
        int: The number of values of L satisfying the given conditions.
    """
    # Maximum boundary for perimeter
    bound = 1500000

    # Limit to reduce unnecessary calculations (m must be less than the square root of the perimeter)
    limit = int((bound / 2)**0.5)

    # Array to track how many triangles can be formed for each perimeter
    triangles = [0] * (bound + 1)

    result = 0

    # Iterate over values of m and n to generate primitive Pythagorean triples
    for m in range(2, limit):
        for n in range(1, m):
            # Check if m and n are coprime (gcd(m, n) == 1) and m + n is odd (to ensure primitive triples)
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                # Calculate the sides of the triangle
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                perimeter = a + b + c

                # Generate multiples of the primitive triple
                while perimeter <= bound:
                    if triangles[perimeter] == 0:
                        triangles[perimeter] = 1
                        result += 1
                    elif triangles[perimeter] == 1:
                        triangles[perimeter] = 2
                        result -= 1
                    perimeter += a + b + c

    return result


if __name__ == "__main__":
    print(f"Problem 75: {compute()}")
