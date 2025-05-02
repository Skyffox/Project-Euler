# pylint: disable=line-too-long
"""
Problem 67: Maximum Path Sum II

Problem description:
This module solves the problem of finding the maximum total from top to bottom in a triangle of one-hundred rows.
The triangle is represented as a list of lists, where each list contains the numbers at each level of the triangle.
The goal is to start from the bottom of the triangle and move upwards, at each step selecting the larger of the two adjacent numbers, 
to ultimately reach the top, obtaining the maximum total sum.

Answer: 7273
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the maximum total from top to bottom in a triangle.
    
    The triangle is read from the file 'inputs/p067_triangle.txt'. 
    The function computes the maximum path sum by starting from the bottom 
    of the triangle and working upwards, updating each element to store 
    the maximum possible sum from that element to the bottom.
    
    Returns:
        int: The maximum path sum starting from the top.
    """
    t = []

    # Read the triangle from a file and store it as a list of lists
    with open('inputs/p067_triangle.txt', 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(' ')
            t.append([int(x) for x in line])

    # Process the triangle from bottom to top
    for i in range(len(t) - 2, -1, -1): # Start from the second-to-last row
        for j in range(i + 1):
            # Update each element with the maximum sum of the two possible paths below
            t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])

    # The top element now contains the maximum path sum
    return t[0][0]


if __name__ == "__main__":
    print(f"Problem 67: {compute()}")
