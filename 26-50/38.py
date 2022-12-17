#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 38.py:


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
