# pylint: disable=line-too-long
"""
Problem 85: Counting Rectangles

Problem description:
We are asked to find the area of the grid that contains the number of rectangles closest to 2 million.

Answer: 2772
"""

from utils import profiler

def approx(x: int, y: int) -> int:
    """
    Computes the total number of rectangles that can be formed in a grid of size x by y.
    This method counts all rectangles of different sizes formed by choosing two horizontal 
    and two vertical lines.

    Args:
        x (int): The number of columns in the grid.
        y (int): The number of rows in the grid.

    Returns:
        int: The total number of rectangles in the grid.
    """
    total = x * y + 1 + x + y # Account for the large rectangles and the borders
    t = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            # Exclude what we already have defined above (the largest rectangles)
            if (i == 1 and j == 1) or (i == 1 and j == y) or (j == 1 and i == x) or (i == x and j == y):
                continue
            x_diff = x - i + 1 # Width difference from right side
            y_diff = y - j + 1 # Height difference from top side
            t += (x_diff * y_diff) # Add all possible smaller rectangles

    return total + t


@profiler
def compute() -> int:
    """
    Finds the area of the grid with the nearest solution to having exactly two million rectangles.

    The function searches through rectangular grids of dimensions between 3 and 120, calculating 
    the number of rectangles each grid contains and finding the grid whose number of rectangles 
    is closest to two million.

    Returns:
        int: The area of the grid.
    """
    # Target number of rectangles
    bound = 2000000
    min_diff = bound
    best_i = 0
    best_j = 0

    # Loop through possible grid sizes (i, j) and compute the difference from the target
    for i in range(3, 120):
        for j in range(i, 120):  # Ensuring j >= i
            p = abs(bound - approx(i, j))  # Difference from target
            if p < min_diff:
                min_diff = p
                best_i = i
                best_j = j

    # Return the area
    return best_i * best_j


if __name__ == "__main__":
    print(f"Problem 85: {compute()}")
