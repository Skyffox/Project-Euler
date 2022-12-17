#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 96.py:
# This program implements a Sudoku solver for a Sudoku of arbitrary size. The
# program also checks whether the found solution is correct.
# To solve a Sudoku you need distinct numbers for each row, column and block in
# the playing grid. The distinct numbers can range from 1 to the length of a
# row. A Sudoku is always played on a square grid.

import fileinput
import math


# Read the input file and store the values as a nested list.
def read_file():
    f = open('p096_sudoku.txt', 'r')
    final_list = []

    for line in f:
        temp_list = []
        line = line.strip()
        try:
           val = int(line[0])
           list_line = [int(d) for d in str(line)]
           for element in list_line:
               if (int(element) == 0):
                   # Give a copy of pos_nums otherwise multiple variables would
                   # point to the same list.
                   temp_list.append([int(element), list(range(1, 10))])
               else:
                   # Give an empty list when the spot has already been filled.
                   temp_list.append([int(element), []])
           final_list[-1].append(temp_list)
        except ValueError:
           final_list.append([])

    return final_list


# Print the board the same way as it was given as input.
def print_grid(grid):
    for row in grid:
        for el in row:
            # Check whether a number contains two digits, for easier spacing.
            if len(str(el[0])) == 2:
                print (el[0], end=" ")
            else:
                print (el[0], end="  ")
        print ("")


# Find a spot in the grid that has not been filled yet. We start at the spot we
# checked last, then we loop over the entire grid again to be sure everything
# is filled in.
def find_next_open_spot(grid, i, j, n):
    for x in range(i, n):
        # Get the next cell in the row.
        for y in range(j+1, n):
            if grid[x][y][0] == 0:
                return x, y
    for x in range(0, n):
        for y in range(0, n):
            if grid[x][y][0] == 0:
                return x, y
    # We are outside the grid, return a magic number.
    return -1, -1


# Function that checks whether a given number can be filled in at a certain
# spot in the grid. To check a block I first find the top left coordinate of
# the block and then loop over the entire block.
def is_valid(grid, i, j, num, n):
    block_size = int(math.sqrt(n))
    # The first part is to check the row the second part to check the column.
    if all([num != grid[i][x][0] and num != grid[x][j][0] for x in range(n)]):
        # Finding the top left x, y coordinates of the section containing
        # the i, j cell with floor division.
        block_x = block_size * (i // block_size)
        block_y = block_size * (j // block_size)
        for x in range(block_x, block_x + block_size):
            for y in range(block_y, block_y + block_size):
                if grid[x][y][0] == num:
                    return False
        return True
    return False


# This function is a lot alike the is_valid() function but that function checks
# whether a given number can be filled in a certain spot. In this function I
# need to check whether every number has been filled in correctly. I do this by
# comparing checks on the rows, columns and blocks with the means of sets.
# Since sets can not contain duplicate elements.
def check_sudoku(grid, n):
    block_size = int(math.sqrt(n))

    for i in range(n):
        row_lst = []
        col_lst = []
        for j in range(n):
            row_lst.append(grid[i][j][0])
            col_lst.append(grid[j][i][0])

            block_lst = []
            block_x = block_size * (i // block_size)
            block_y = block_size * (j // block_size)
            for x in range(block_x, block_x + block_size):
                for y in range(block_y, block_y + block_size):
                    block_lst.append(grid[x][y][0])

            # Check whether the length of a set is the same as the list. I do
            # this to check for duplicates.
            if len(set(row_lst)) == len(row_lst):
                if len(set(col_lst)) == len(col_lst):
                    if not len(set(block_lst)) == len(block_lst):
                        return False
    return True


# To solve the Sudoku I search for the next open spot in the grid. For each
# open spot in the grid I keep a list of numbers that are still possible to put
# in that spot. When an open spot is found I loop over the list of possible
# numbers, if the length of that list is one then there is only one solution
# for that open spot. When the numbers in the list of possible numbers are not
# possible anymore they are removed from the list. When all spots have been
# filled in I check the sudoku to see if it is a valid solution.
def solve_sudoku(grid, i, j, n):
    while True:
        i, j = find_next_open_spot(grid, i, j, n)
        # All spots have been filled, check it now.
        if i == -1 and j == -1:
            if check_sudoku(grid, n):
                return True
            return False
        # Loop over possible solutions for the spot.
        for num in grid[i][j][1]:
            if is_valid(grid, i, j, num, n):
                if (len(grid[i][j][1]) == 1):
                    grid[i][j][0] = num
                    grid[i][j][1] = []
            else:
                # Delete the number from the list of possible numbers.
                if (num in grid[i][j][1]):
                    grid[i][j][1].remove(num)
    return False


# Get the grid and the length of the grid and check whether this is solvable.
grids = read_file()

for grid in grids:

    print ("This is the input sudoku:\n")
    print_grid(grid)

    solvable = solve_sudoku(grid, 0, 0, 9)

    if solvable is True:
        print ("This is the output sudoku:\n")
        print_grid(grid)

    print("\n\n")
    break
