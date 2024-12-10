# Let p(n) represent the number of different ways in which n coins can be separated into piles. 
# Find the least value of n for which p(n) is divisible by one million.
# Execution time: ???

# https://stackoverflow.com/questions/52167339/get-all-possible-str-partitions-of-any-length


def partitions(lst, n):
    lst_n = n

    while len(lst[0]) is not 1:
        for c, i in enumerate(reversed(lst)):
            if len(i) == 1:
                lst[n-2-c].pop()
                lst[n-1-c].append(1)

        break


partitions([[1] * 5], 5)
