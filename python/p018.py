# pylint: disable=line-too-long
"""
Problem 18: Find the maximum total from top to bottom of the triangle below
Answer: 
Execution time: 0.0000s
"""

from utils import profiler


def rec_sum_at_row(row_data, row_num):
    """Define a recursive function to create partial sums by row"""
    for i in range(len(row_data[row_num])):
        # Add the largest of the values below-left or below-right
        row_data[row_num][i] += max([row_data[row_num + 1][i], row_data[row_num + 1][i + 1]])
    if len(row_data[row_num]) == 1:
        return row_data[row_num][0]

    return rec_sum_at_row(row_data, row_num-1)


@profiler
def compute():
    """Load the entire pyramid"""
    rows = []
    with open("inputs/problem-18-data", "r", encoding="utf-8") as file:
        for line in file:
            rows.append([int(i) for i in line.rstrip('\n').split(" ")])

    # Start at second to last row
    return rec_sum_at_row(rows, len(rows)-2)


if __name__ == "__main__":
    print(f"Problem 18: {compute()}")
