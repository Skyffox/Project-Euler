# pylint: disable=line-too-long
"""
Problem 83: Path sum: four ways

Problem description:
This solution solves the minimal path sum problem where the goal is to find the minimal path 
from the top-left to the bottom-right corner of a grid. The path can only move right, down, 
or left. This solution uses Dijkstra's algorithm with a priority queue (min-heap) to efficiently 
find the minimal path sum.

Answer: 425185
"""

import heapq
from typing import List
from utils import profiler


def minimal_path_sum(grid: List[List[int]]) -> int:
    """
    Finds the minimal path sum from the top-left to the bottom-right of a grid using Dijkstra's algorithm.
    
    Starting from the top-left corner, this function computes the minimal path sum for each element 
    in the grid by exploring valid moves (right, down, left, up) using a priority queue (min-heap).

    Args:
        grid (list of list of int): A 2D grid representing the cost of each cell in the path.

    Returns:
        int: The minimal path sum from the top-left to the bottom-right corner of the grid.
    """
    n = len(grid)

    # Create a priority queue (min-heap) for Dijkstra's algorithm.
    pq = []

    # Initialize the priority queue with the top-left element.
    heapq.heappush(pq, (grid[0][0], 0, 0))  # (cost, row, col)

    # Create a distance table to store the minimal cost to each cell.
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = grid[0][0]  # Starting point

    # Directions for moving in 4 directions: right, down, left, and up.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Dijkstra's algorithm to find the minimal path sum.
    while pq:
        current_dist, row, col = heapq.heappop(pq)

        # If we reach the bottom-right corner, return the current distance.
        if row == n - 1 and col == n - 1:
            return current_dist

        # Explore all 4 possible neighbors.
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:
                # Calculate the new distance.
                new_dist = current_dist + grid[new_row][new_col]

                # If a shorter path is found, update the distance table and push to the priority queue.
                if new_dist < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_dist
                    heapq.heappush(pq, (new_dist, new_row, new_col))

    # If the loop finishes, return the minimum value in the last row as the result.
    return min(dist[n-1])


@profiler
def compute() -> int:
    """
    Reads the grid from the input file and computes the minimal path sum for Problem 83.
    
    This function reads the grid from the file "inputs/p081_matrix.txt", where each line of the grid 
    is separated by commas. It then calculates the minimal path sum using the `minimal_path_sum` function.

    Returns:
        int: The minimal path sum for the given input grid.
    """
    # Read the grid from the input file.
    grid = []
    with open("inputs/p081_matrix.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = list(map(int, line.strip().split(",")))
            grid.append(line)

    # Solve the problem using minimal_path_sum and return the result.
    return minimal_path_sum(grid)


if __name__ == "__main__":
    print(f"Problem 83: {compute()}")
