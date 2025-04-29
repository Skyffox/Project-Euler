# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
# What is the maximum 16-digit string for a "magic" 5-gon ring?
# Execution time: 1.658s

import itertools

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

permu = list(itertools.permutations(nums, 10))
reversed_permu = list(reversed(permu))
solution = None

# Convert a tuple to a number.
def tuples_to_num(tuple):
    return ''.join(''.join(str(i) for i in tuple))


# Do all the checks for the magic 5-gon circle.
def check(p):
    # Can not be a 10 in the circle since it would be count twice.
    if p[1] == 10 or p[2] == 10 or p[4] == 10 or p[6] == 10 or p[8] == 10:
        return False

    # First position needs to be smaller.
    if p[0] > p[3] or p[0] > p[5] or p[0] > p[7] or p[0] > p[9]:
        return False

    # Count the length of the sides.
    if p[0] + p[1] + p[2] != p[3] + p[2] + p[4]:
        return False
    if p[0] + p[1] + p[2] != p[5] + p[4] + p[6]:
        return False
    if p[0] + p[1] + p[2] != p[7] + p[6] + p[8]:
        return False
    if p[0] + p[1] + p[2] != p[9] + p[8] + p[1]:
        return False

    return True


# Traverse all permutations.
for p in reversed_permu:
    if check(p):
        # Form the complete string.
        solution = [p[0], p[1], p[2], p[3], p[2], p[4], p[5], p[4],
                    p[6], p[7], p[6], p[8], p[9], p[8], p[1]]

    if solution:
        break

print("Maximum string:", tuples_to_num(solution))
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
