#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 61.py:
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which
# each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
# is represented by a different number in the set.


# Return a triangle number.
def triangle(n):
    return n * (n + 1) / 2


# Return a square number.
def square(n):
    return n ** 2


# Return a pentagonal number.
def pentagonal(n):
    return n * (3 * n - 1) / 2


# Return a hexagonal number.
def hexagonal(n):
    return n * (2 * n - 1)


# Return a heptagonal number.
def heptagonal(n):
    return n * (5 * n - 3) / 2


# Return a octagonal number.
def octagonal(n):
    return n * (3 * n - 2)


# Find interval where each function returns a list of four digit numbers.
tri = [int(triangle(x)) for x in range(45, 141)]
squares = [int(square(x)) for x in range(32, 100)]
penta = [int(pentagonal(x)) for x in range(26, 82)]
hexa = [int(hexagonal(x)) for x in range(23, 71)]
hepta = [int(heptagonal(x)) for x in range(21, 64)]
octa = [int(octagonal(x)) for x in range(19, 59)]

all_lst = [squares, penta, hexa, hepta, octa]


def find_candidates(num, indices):
    last = [int(x) for x in str(num)][2:]
    candidates = []

    for idx, lst in enumerate(all_lst):
        if idx in indices:
            continue

        for l in lst:
            first = [int(x) for x in str(l)][:2]

            if first == last:
                candidates.append([l, idx])

    return candidates


for t in tri:
    candidates = find_candidates(t, [])
    idx_lst = []

    for c1 in candidates:
        n1 = find_candidates(c1[0], idx_lst)

        if len(n1) == 0 or c1[1] in idx_lst:
            continue

        for c2 in n1:
            idx_lst = [c1[1]]
            n2 = find_candidates(c2[0], idx_lst)

            if len(n2) == 0 or c2[1] in idx_lst:
                continue

            for c3 in n2:
                idx_lst = [c1[1], c2[1]]
                n3 = find_candidates(c3[0], idx_lst)

                if len(n3) == 0 or c3[1] in idx_lst:
                    continue

                for c4 in n3:
                    idx_lst = [c1[1], c2[1], c3[1]]
                    n4 = find_candidates(c4[0], idx_lst)

                    if len(n4) == 0 or c4[1] in idx_lst:
                        continue

                    for c5 in n4:
                        idx_lst = [c1[1], c2[1], c3[1], c4[1]]

                        if c5[1] in idx_lst:
                            continue

                        first = [int(x) for x in str(t)][:2]
                        last = [int(x) for x in str(c5[0])][2:]

                        if first == last:
                            final_lst = [t, c1[0], c2[0], c3[0], c4[0], c5[0]]
                            print("Sum of cyclic list:", sum(final_lst))
