# You need to:

# Generate all prime numbers up to a certain limit.
# Use these primes to count the number of ways to express a number as a sum of primes.
# Find the smallest number that has more than 5000 such representations.
# Execution time: ???

from utils import sieve_of_atkin

# This function uses dynamic programming to count the number of ways each number up to the limit can be expressed as the sum of primes. The list ways holds the number of ways each number can be formed using the primes.
def count_prime_sum_ways(limit, primes):
    """Count the number of ways to sum primes to get each number up to `limit`."""
    # Create a list to store the number of ways for each number up to `limit`
    ways = [0] * (limit + 1)
    ways[0] = 1  # There is one way to get 0, by not using any primes
    
    # Dynamic programming approach to count sums
    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]
    
    return ways

# This function uses the previous two functions. It returns the smallest number that can be expressed as a sum of primes in more than n ways, where n is 5000 in this case.
# The limit of 100 used in the code may need adjustment based on your computational constraints. You can increase it if the solution isn't found or if you're optimizing performance.
def compute():
    """Find the smallest number that can be written as a sum of primes in more than `n` ways."""
    primes = sieve_of_atkin(100)
    ways = count_prime_sum_ways(100, primes)
    
    for i in range(2, 100 + 1):
        if ways[i] > 5000:
            return i
    return None

# We want to find the first number that can be expressed as a sum of primes in more than 5000 ways.
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
