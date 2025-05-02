# pylint: disable=line-too-long
"""
Problem 28: Number Spiral Diagonals

Problem description:
Starting with the number 1 and moving to the right in a clockwise direction, a 5 by 5 spiral is formed as follows:

21 22 23 24 25  
20  7  8  9 10  
19  6  1  2 11  
18  5  4  3 12  
17 16 15 14 13  

It can be verified that the sum of the numbers on the diagonals is 101.  
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Answer: 669171001
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the sum of the numbers on the diagonals in a 1001 by 1001 number spiral.
    
    The spiral is formed starting with the number 1 and moving clockwise, and the sum of the numbers 
    along the diagonals is computed as the spiral grows.
    
    The function iterates through each layer of the spiral, adding up the numbers that appear on the diagonals
    in the spiral's layers. The spiral's side length increases by 2 each time, and the numbers on the diagonals 
    are added to the total sum.
    
    Returns:
        int: The sum of the numbers on the diagonals of a 1001 by 1001 spiral.
    """
    total_sum = 1 # Initialize sum with the center value (1)
    current_number = 1 # Start with the first number in the spiral (1)
    step_size = 2 # Initial difference between diagonal numbers

    # Loop through the layers of the spiral (starting from size 3 up to size 1001)
    for _ in range(3, 1002, 2):
        # Add the numbers at the 4 diagonal positions for each layer
        for _ in range(4):
            current_number += step_size
            total_sum += current_number

        # Increase the step size for the next layer
        step_size += 2

    return total_sum


if __name__ == "__main__":
    print(f"Problem 28: {compute()}")
