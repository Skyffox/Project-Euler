# pylint: disable=line-too-long
"""
Problem 96: Sudoku - The Millionaire's Club

Problem description:
In the 96th problem of Project Euler, we are given a list of 50 Sudoku grids. Each grid is partially filled, and we are tasked with solving the Sudoku puzzles.
For each puzzle, after solving it, we must take the first three digits of the top-left 3x3 subgrid and sum them.

Answer: 24702
"""

from utils import profiler

def read_file():
    """Reads the input file containing multiple Sudoku grids and returns a list of them."""
    all_grids, grid = [], []
    with open('inputs/p096_sudoku.txt', "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.find("Grid") != -1:
                if grid:
                    all_grids.append(grid)
                grid = []
            else:
                grid.append(list(map(int, str(line))))

        all_grids.append(grid)  # Add the last grid

    return all_grids

def is_valid(grid, num, row, col):
    """Check if it's valid to place num in the position (row, col) of the Sudoku grid."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(grid):
    """Find the next empty cell in the grid (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j  # Return the row and column of the empty cell
    return None  # No empty cells left, puzzle is solved

def solve(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty(grid)

    # If there are no empty cells, the puzzle is solved
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(grid, num, row, col):
            grid[row][col] = num  # Place the number

            if solve(grid):  # Recursively solve the rest of the puzzle
                return True

            # If not solvable, backtrack by resetting the cell
            grid[row][col] = 0

    return False  # Trigger backtracking if no number works

@profiler
def compute():
    """Solve all Sudoku grids and return the sum of the top-left three digits of each solved grid."""
    grids = read_file()
    total_sum = 0

    for grid in grids:
        solvable = solve(grid)

        if solvable:
            # Sum the first three digits of the top-left 3x3 subgrid
            num = int("".join(map(str, grid[0][:3])))
            total_sum += num

    return total_sum

if __name__ == "__main__":
    print(f"Problem 96: {compute()}")
