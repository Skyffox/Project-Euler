# Take the number 192 and multiply it by each of 1, 2, and 3:
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5)
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
# Execution time: 0.261s

BIGGEST_OUTCOME = 987654321

outcomes = []
for n in range(2, 20000):
    prod = ''
    tmp = ''
    add = True

    for i in range(1, 9):
        prod += str(n*i)

        if int(prod) > BIGGEST_OUTCOME:
            break

        tmp = prod

    # Check if it is a pandigital number.
    if len(set(list(tmp))) == 9 and len(list(tmp)) == 9:
        tmp_lst = [int(x) for x in tmp]
        for i in range(1, 10):
            if i not in tmp_lst:
                add = False
                break

        if add:
            outcomes.append(tmp)

# Print largest pandigital number.
print(sorted([int(x) for x in outcomes])[-1])
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
