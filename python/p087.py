# pylint: disable=no-name-in-module, line-too-long
"""
Problem 87: Prime Power Triples

Problem description:
This problem involves finding how many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power. The task is to determine how many distinct numbers can be expressed in this way.

Answer: 1097343
"""

from utils import profiler, sieve_of_atkin


@profiler
def compute() -> int:
    """
    Computes how many distinct numbers below 50 million can be expressed as the sum of a prime square, prime cube,
    and prime fourth power.

    The algorithm uses the Sieve of Atkin to generate prime numbers, then iterates through combinations of prime squares,
    cubes, and fourth powers to find numbers that satisfy the condition. It returns the count of distinct numbers.
    
    Returns:
    int: The count of distinct numbers below 50 million that can be expressed as the sum of a prime square, prime cube, and prime fourth power.
    """
    bound = 50000000 # Upper bound for the numbers we are interested in
    limit = int((bound - (2**3) - (2**4))**0.5) # Limit for the sieve (for prime squares, cubes, and fourth powers)

    # Get the list of primes using the sieve of Atkin
    primes = sieve_of_atkin(limit)

    # Set to store the distinct numbers
    nums = set()

    # Iterate over primes for square, cube, and fourth power
    for i in primes:
        square = pow(i, 2)
        if square > bound:
            break
        for j in primes:
            cube = pow(j, 3)
            if square + cube > bound:
                break
            for k in primes:
                fourth_power = pow(k, 4)
                p = square + cube + fourth_power
                if p > bound:
                    break
                nums.add(p)

    # Return the count of distinct numbers
    return len(nums)


if __name__ == "__main__":
    print(f"Problem 87: {compute()}")
