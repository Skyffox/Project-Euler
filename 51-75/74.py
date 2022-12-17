#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 74.py:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sum_of_fac(n):
    res = [int(x) for x in str(n)]
    return sum([fac[y] for y in res])


fac = [factorial(i) for i in range(0, 10)]

ans = 0
for i in range(2, 1000001):
    chain = 1
    seen = [i]
    s = sum_of_fac(i)
    not_break = True

    while True:
        seen.append(s)
        s = sum_of_fac(s)
        chain += 1
        if s in seen:
            break
        if chain > 60:
            not_break = False
            break

    if chain == 60 and not_break:
        ans += 1

print(ans)
