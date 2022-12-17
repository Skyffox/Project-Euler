#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 112.py:

bouncy = 0
total = 101

while True:
    UP = False
    DOWN = False

    lst = list(str(total))
    first = lst[0]

    for n in lst[1:]:
        if n < first:
            DOWN = True
        elif n > first:
            UP = True

        first = n

    if UP and DOWN:
        bouncy += 1

    proportion = bouncy / total

    if proportion > 0.99:
        break

    total += 1

print("Number of bouncy numbers:", bouncy)
print("Total numbers:", total)
print("Proportion of bouncy numbers", bouncy / total * 100)
