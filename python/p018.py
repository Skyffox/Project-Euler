# pylint: disable=line-too-long
"""
Problem 18: Maximum Path Sum I

Problem description:
Find the maximum total from top to bottom of the triangle below by starting at the top and moving to adjacent numbers on the row below. 
Each step you may move to an adjacent number in the row below. 
The path must move to adjacent numbers, one per row, and the total sum needs to be maximized.

Answer: 1074
"""

from typing import List
from utils import profiler


@profiler
def compute() -> int:
    """
    Load the triangle data from a file and apply a bottom-up dynamic programming approach 
    to find the maximum path sum from the top to the base.

    This function reads a triangle from the file "inputs/problem-18-data", which consists 
    of integers arranged in rows, and calculates the maximum path sum by starting from 
    the second-to-last row and working upwards. Each element in the current row is updated 
    by adding the maximum of the two elements directly below it. The top element of the 
    triangle will then contain the maximum sum.

    Returns:
        int: The maximum path sum from the top to the base of the triangle.
    """
    # Load the triangle data from file
    rows: List[List[int]] = []
    with open("inputs/problem-18-data", "r", encoding="utf-8") as file:
        for line in file:
            rows.append([int(i) for i in line.rstrip('\n').split()])

    # Start from the second-to-last row and move upwards
    for row in range(len(rows) - 2, -1, -1):
        for i in range(len(rows[row])):
            # Update each element by adding the maximum of the two elements below it
            rows[row][i] += max(rows[row + 1][i], rows[row + 1][i + 1])

    # The top element now contains the maximum total
    return rows[0][0]


if __name__ == "__main__":
    print(f"Problem 18: {compute()}")
