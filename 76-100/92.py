#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 92.py:

def square_digits(n):
    total = 0
    while n > 0:
        digit = int(n % 10)
        total += digit*digit
        n = int(n / 10)

    return total

eight_nine = []
all1 = []
all2 = []
for i in range(2, 10000000):
    start = i
    l1 = []
    l2 = []
    while i != 89 and i != 1:
        i = square_digits(i)
        l1.append(i)
        l2.append(i)

        if i in all1:
            all1.extend(l1)
            eight_nine.append(start)
            break
        if i in all2:
            all2.extend(l2)
            break

    if i == 89:
        eight_nine.append(start)

print(len(set(eight_nine)))
