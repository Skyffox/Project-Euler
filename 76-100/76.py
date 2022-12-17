#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 76.py:

# same soluiton as problem 31
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


3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
