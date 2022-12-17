#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 109.py:

singles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
doubles = [x * 2 for x in singles]
triples = [x * 3 for x in singles]

# Bullseye
singles.append(25)
doubles.append(50)

total = 0

for checkout in range(2, 100):
    solutions = []

    # Only doubles
    for first in doubles:
        if checkout - first < 0: break
        if checkout - first == 0:
            x = first / 2
            solutions.append(["D" + str(int(x))])

    # First is single last is double
    for first in singles:
        if checkout - first < 0: break
        for second in doubles:
            if checkout - first - second < 0: break
            if checkout - first - second == 0:
                y = second / 2
                solutions.append(["S" + str(first), "D" + str(int(y))])

    # First is double last is double
    for first in doubles:
        if checkout - first < 0: break
        for second in doubles:
            if checkout - first - second < 0: break
            if checkout - first - second == 0:
                x = first / 2
                y = second / 2
                solutions.append(["D" + str(int(x)), "D" + str(int(y))])

    # First is triple last is double
    for first in triples:
        if checkout - first < 0: break
        for second in doubles:
            if checkout - first - second < 0: break
            if checkout - first - second == 0:
                x = first / 3
                y = second / 2
                solutions.append(["T" + str(int(x)), "D" + str(int(y))])

    # First is single second is single last is double
    for first in singles:
        if checkout - first < 0: break
        for second in singles:
            if checkout - first - second < 0: break
            for third in doubles:
                if checkout - first - second - third < 0: break
                if checkout - first - second - third == 0:
                    z = third / 2
                    solutions.append(["S" + str(first), "S" + str(second), "D" + str(int(z))])

    # First is single second is double last is double
    for first in singles:
        if checkout - first < 0: break
        for second in doubles:
            if checkout - first - second < 0: break
            for third in doubles:
                if checkout - first - second - third < 0: break
                if checkout - first - second - third == 0:
                    y = second / 2
                    z = third / 2
                    solutions.append(["S" + str(first), "D" + str(int(y)), "D" + str(int(z))])

    # First is single second is triple last is double
    for first in singles:
        if checkout - first < 0: break
        for second in triples:
            if checkout - first - second < 0: break
            for third in doubles:
                if checkout - first - second - third < 0: break
                if checkout - first - second - third == 0:
                    y = second / 3
                    z = third / 2
                    solutions.append(["S" + str(first), "T" + str(int(y)), "D" + str(int(z))])

    # First is double second is double last is double
    for first in doubles:
        if checkout - first < 0: break
        for second in doubles:
            if checkout - first - second < 0: break
            for third in doubles:
                if checkout - first - second - third < 0: break
                if checkout - first - second - third == 0:
                    x = first / 2
                    y = second / 2
                    z = third / 2
                    solutions.append(["D" + str(int(x)), "D" + str(int(y)), "D" + str(int(z))])

    # First is double second is triple last is double
    for first in doubles:
        if checkout - first < 0: break
        for second in triples:
            if checkout - first - second < 0: break
            for third in doubles:
                if checkout - first - second - third < 0: break
                if checkout - first - second - third == 0:
                    x = first / 2
                    y = third / 3
                    z = third / 2
                    solutions.append(["D" + str(int(x)), "T" + str(int(y)), "D" + str(int(z))])

    # First is triple second is triple last is double
    for first in triples:
        if checkout - first < 0: break
        for second in triples:
            if checkout - first - second < 0: break
            for third in doubles:
                if checkout - first - second - third < 0: break
                if checkout - first - second - third == 0:
                    x = first / 3
                    y = second / 3
                    z = third / 2
                    solutions.append(["T" + str(int(x)), "T" + str(int(y)), "D" + str(int(z))])


    len3solutions = [sublst for sublst in solutions if len(sublst) == 3]
    othersolutions = [sublst for sublst in solutions if len(sublst) != 3]

    new_solutions = []
    for sol in len3solutions:
        first_two = sorted(sol[:2])
        first_two.append(sol[2])
        if first_two not in new_solutions:
            new_solutions.append(first_two)

    total += len(othersolutions) + len(new_solutions)

# Print the solutions
# for sol in othersolutions:
#     print(sol, end="\n")
#
# for sol in new_solutions:
#     print(sol, end="\n")


print("Number of solutions found:", total)
