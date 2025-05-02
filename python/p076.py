# pylint: disable=line-too-long
"""
Problem 76: Counting Summations

Problem description:
The problem asks how many different ways 100 can be written as the sum of at least two positive integers. 
This is essentially a problem of finding integer partitions, where the order of the summands doesn't matter, and no part is used more than once.

Answer: 190569291
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the number of ways 100 can be written as the sum of at least two positive integers, 
    using dynamic programming for efficient calculation.
    
    Returns:
        int: The result for writing 100 as a sum of at least two positive integers.
    """
    total = 100
    # DP array where dp[i] represents the number of ways to write i as a sum of integers
    dp = [0] * (total + 1)
    dp[0] = 1 # Base case: there is 1 way to sum to 0 (the empty sum)

    # Update the dp array using all integers from 1 to total
    for i in range(1, total):
        for j in range(i, total + 1):
            dp[j] += dp[j - i]

    # Return the number of ways to write 100 as the sum of at least two integers
    return dp[total]


if __name__ == "__main__":
    print(f"Problem 76: {compute()}")
