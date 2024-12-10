# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
# Find the least number for which the proportion of bouncy numbers is exactly 99%.
# Execution time: 3.825s

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
