# pylint: disable=line-too-long
"""
Problem 82: Path sum: Three Ways

Problem description:
This solution solves the minimal path sum problem where the goal is to find the minimal path 
from any cell in the top row to any cell in the bottom row of a grid. The path can move down, 
left, or right. This solution uses Dijkstra's algorithm with a priority queue 
(min-heap) to efficiently find the minimal path sum.

Answer: 260324
"""

import heapq
from typing import List
from utils import profiler


def minimal_path_sum(grid: List[List[int]]) -> int:
    """
    Finds the minimal path sum from the top row to the bottom row of a grid using Dijkstra's algorithm.
    
    Starting from any position in the top row, this function computes the minimal path sum for each element 
    in the grid by exploring valid moves (down, left, right) using a priority queue (min-heap).

    Args:
        grid (list of list of int): A 2D grid representing the cost of each cell in the path.

    Returns:
        int: The minimal path sum from any cell in the top row to any cell in the bottom row of the grid.
    """
    n = len(grid)

    # Create a priority queue (min-heap) for Dijkstra's algorithm.
    pq = []

    # Initialize the priority queue with all elements in the top row.
    for j in range(n):
        heapq.heappush(pq, (grid[0][j], 0, j)) # (cost, row, col)

    # Create a distance table to store the minimal cost to each cell.
    dist = [[float('inf')] * n for _ in range(n)] # Distance table initialized to infinity
    for j in range(n):
        dist[0][j] = grid[0][j] # Starting from the top row

    # Directions for moving in 3 directions: down, left, right.
    directions = [(1, 0), (0, -1), (0, 1)] # Down, Left, Right

    # Dijkstra's algorithm to find the minimal path sum.
    while pq:
        current_dist, row, col = heapq.heappop(pq)

        # If we reach the bottom row, return the current distance.
        if row == n - 1:
            return current_dist

        # Explore all valid neighbors (down, left, right).
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:
                # Calculate the new distance.
                new_dist = current_dist + grid[new_row][new_col]

                # If a shorter path is found, update the distance table and push to the priority queue.
                if new_dist < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_dist
                    heapq.heappush(pq, (new_dist, new_row, new_col))

    # If the loop finishes, return the minimal path sum for the bottom row.
    return min(dist[n-1])


@profiler
def compute() -> int:
    """
    Reads the grid from the input file and computes the minimal path sum for Problem 82.
    
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

    # Transpose the matrix using zip and list comprehension
    transposed_matrix = [list(row) for row in zip(*grid)]

    # Solve the problem using minimal_path_sum and return the result.
    return minimal_path_sum(transposed_matrix)


if __name__ == "__main__":
    print(f"Problem 82: {compute()}")
