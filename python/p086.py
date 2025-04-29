# Given a cuboid with integer dimensions 𝑎, 𝑏, and 𝑐 (where 𝑎, 𝑏, and 𝑐 are positive integers), the shortest path from one corner to the opposite corner is given by the 3D distance formula:
# distance = (𝑎^2 + 𝑏^2 + 𝑐^2)^0.5 
# The task is to find all cuboids where this distance is an integer. The problem also asks us to determine how many such cuboids exist for perimeters of the cuboids, where:
# perimeter = 𝑎 + 𝑏 + 𝑐
# The challenge is to find the smallest perimeter where the number of such cuboids exceeds 1000.

# Key Insights:
# The shortest path between two opposite corners of the cuboid is (𝑎^2 + 𝑏^2 + 𝑐^2)^0.5, and we need this to be an integer (i.e., the sum of squares should be a perfect square).
# The task is essentially asking for how many such cuboids exist for various perimeters, and you are tasked to find the minimum perimeter that results in more than 1000 cuboids.

import itertools
import functools
import math

# https://martin-ueding.de/posts/project-euler-solution-86-cuboid-route/

def is_square(number: int) -> bool:
    floor = int(math.sqrt(number))
    return floor**2 == number

@functools.cache
def shortest_path_is_integer(a, b_plus_c) -> bool:
    return is_square(a**2 + b_plus_c**2)

# The check whether it is an integer path length only depends on a and b+c. 
# There is no real need to check all combinations of b and c, 
# we just need to check once for their sum and then multiply it with the number of (b,c)
# there are such that M ≥ a ≥ b ≥ c
def multiplicity(a: int, b_plus_c: int) -> int:
    if b_plus_c <= a + 1:
        return b_plus_c // 2
    else:
        return (2 * a - b_plus_c + 2) // 2


def compute() -> int:
    ceiling = 1_000_000
    result = 0
    for a in itertools.count(1):
        for b_plus_c in range(1, 2 * a + 1):
            if shortest_path_is_integer(a, b_plus_c):
                result += multiplicity(a, b_plus_c)
                if result > ceiling:
                    return a

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
