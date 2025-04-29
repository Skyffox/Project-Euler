# How many different ways can one hundred be written as a sum of at least two positive integers?
# Execution time: 91.166s

# Same solution as problem 31.
def count(total, s, size):
    if (total < 0):
        return 0
    if (total == 0):
        return 1
    if (size == 1):
        return 1
    else:
        # Go through each possible combination
        return count(total, s, size-1) + count(total-s[size-1], s, size)


lst = list(range(1, 100))
print(count(100, lst, len(lst)))

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
