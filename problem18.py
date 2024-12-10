# Find the maximum total from top to bottom of the triangle below:
# Execution time: 0.241s

# Define a recursive function to create partial sums by row
def rec_sum_at_row(row_data, row_num):
    # Iterate over the given row
    for i in range(len(row_data[row_num])):
        # Add the largest of the values below-left or below-right
        row_data[row_num][i] += max([row_data[row_num+1][i], row_data[row_num+1][i+1]])
    # base case
    if len(row_data[row_num]) == 1:
        return row_data[row_num][0]
    # recursive case
    else:
        return rec_sum_at_row(row_data, row_num-1)


rows = []
with open('inputs/problem-18-data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])

result = rec_sum_at_row(rows, len(rows)-2) # start at second to last row
print(result)
