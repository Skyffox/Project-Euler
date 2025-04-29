# Execution time: ???

from copy import deepcopy

# Read the input file and store the values as a nested list.
def read_file():
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

        all_grids.append(grid)

    return all_grids


def is_valid(grid, num, row, col):
    """Check if it's valid to place num in the position (row, col)."""
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
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

# Get the grid and the length of the grid and check whether this is solvable.
def compute():
    grids = read_file()
    s = 0

    for grid in grids:
        solvable = solve(grid)

        if solvable:
            num = int("".join(map(str, [grid[0][0], grid[0][1], grid[0][2]])))
            s += num

    return s


if __name__ == "__main__":
    print(f"Problem 96: {compute()}")
