# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?
# Execution time: 0.222s

# Contains the sum of all the diagonals
sum = 1

# Contains a number from the diagonals
num = 1
# Starting differences between diagonal numbers
difference = 2

# Loop over amount of diagonals
for i in range(3, 1002, 2):
    # 4 diagonals per n of row/col to loop over
    for j in range(1, 5):
        # Add the difference to come to a diagonal
        num += difference
        # Add the number in the diagonal
        sum += num
    # Added lines when a col/row is added
    difference += 2
    
print(sum)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
