# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.
# Execution time: 7.861s

def issquare(n):
    root = int(n**0.5)
    if root**2 == n:
        return True
    return False


def create_num(n):
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    i = 1
    insert = list(str(n))
    for j in insert:
        lst.insert(i, j)
        i += 2

    return int("".join(lst))

# Max insert numbers
it = 999999999

while it > 0:
    n = create_num(it)
    if issquare(n):
        break

    it -= 1

print("Unique positive integer:", n**0.5)
