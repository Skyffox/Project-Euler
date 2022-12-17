#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 78.py:

# https://stackoverflow.com/questions/52167339/get-all-possible-str-partitions-of-any-length

# def partitions(s):
#     for i in range(1, len(s)+1):
#         first, rest = s[:i], s[i:]
#         for p in partitions(rest):
#             yield [first] + p


def partitions(lst, n):
    lst_n = n
    # print(len(lst))
    while len(lst[0]) is not 1:
        # lst = [[1,1,1,1], [1]]
        # n = len(lst)
        for c, i in enumerate(reversed(lst)):
            if len(i) == 1:
                lst[n-2-c].pop()
                lst[n-1-c].append(1)

        break


partitions([[1] * 5], 5)
