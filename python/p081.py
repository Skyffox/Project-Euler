# pylint: disable=line-too-long
"""
Problem 81: Path Sum: Two Ways

Problem Description:
The task is to find the minimal path sum from the top-left to the bottom-right 
of a grid, moving only right or down. The function computes this minimal sum 
using Dijkstra's algorithm to efficiently explore the grid.

Answer: 427337
"""

import heapq
from typing import List
from utils import profiler


def minimal_path_sum(grid: List[List[int]]) -> int:
    """
    Finds the minimal path sum from the top-left to the bottom-right of a grid, 
    where you can only move right or down at each step.

    This implementation uses Dijkstra's algorithm to calculate the minimal path sum.
    
    Args:
        grid (list of list of int): A 2D grid where each value represents the cost of stepping into that cell.
        
    Returns:
        int: The minimal path sum from the top-left to the bottom-right of the grid.
    """
    n = len(grid)

    # Initialize a priority queue (min-heap) for Dijkstra's algorithm
    pq = [(grid[0][0], 0, 0)] # (cost, row, col)

    # Distance table to store the minimal cost to reach each cell
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = grid[0][0] # Starting point

    # Directions for moving right and down
    directions = [(0, 1), (1, 0)]

    # Dijkstra's algorithm to find the minimal path sum
    while pq:
        current_dist, row, col = heapq.heappop(pq)

        # If we reach the bottom-right corner, return the minimal cost
        if row == n - 1 and col == n - 1:
            return current_dist

        # Explore neighboring cells (right and down)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:
                # Calculate the new distance
                new_dist = current_dist + grid[new_row][new_col]
                # If a shorter path is found, update the distance table and push to the queue
                if new_dist < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_dist
                    heapq.heappush(pq, (new_dist, new_row, new_col))

    # If the loop finishes without reaching the target, return the minimal distance in the last row
    return dist[n-1][n-1]


@profiler
def compute() -> int:
    """
    Reads the matrix from a file and computes the minimal path sum.
    
    Returns:
        int: The minimal path sum for the given input grid.
    """
    # Read the grid from the input file
    grid = []
    with open("inputs/p081_matrix.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = list(map(int, line.strip().split(",")))
            grid.append(line)

    # Solve the problem using minimal_path_sum
    return minimal_path_sum(grid)


if __name__ == "__main__":
    print(f"Problem 81: {compute()}")
