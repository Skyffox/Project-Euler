#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 79.py:

f = open('p079_keylog.txt', 'r')

keys = []
for line in f:
    line = line.strip()
    keys.append(int(line))

keys = sorted(list(set(keys)))

first = []
second = []
third = []
for key in keys:
    first.append(int(str(key)[0:1]))
    second.append(int(str(key)[1:2]))
    third.append(int(str(key)[2:3]))


permutations = []
for it, x in enumerate(first):
    permutations.append([x, second[it]])
    permutations.append([x, third[it]])
    permutations.append([second[it], third[it]])

# remove duplicates
fnl = [list(i) for i in set(map(tuple, permutations))]
all_nums = list(set(first + second + third))

# From here on out we create a new list which checks how many characters come
# before the current character, then we sort the list on the least characters
lst = []
for i in all_nums:
    length = 0
    for j in fnl:
        if i == j[1]:
            length += 1
    lst.append([i, length])

lst = sorted(lst, key=lambda x: x[1])
passcode = [i[0] for i in lst]
print("Passcode:", passcode)
