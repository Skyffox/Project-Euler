#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 95.py:

def proper_divisors(n):
    # Note that this loop runs till square root
    i = 1
    lst = []
    while i <= (n**0.5):
        if (n % i == 0):
            # If divisors are equal
            if (n / i == i):
                lst.append(i)
            else:
                lst.append(i)
                if (n / i != n):
                    lst.append(int(n / i))
        i = i + 1

    return sum(lst)


best = 0
perfect_numbers = [1]
for i in range(2, 600000): 
    s = proper_divisors(i)
    lst_len = 1
    lst = [i]
    seen = [s]
    while s != i:
        old_s = s
        lst.append(s)
        s = proper_divisors(s)

        if s > 1000000 or s in seen:
            lst_len = 0
            break
        if s == old_s:
            perfect_numbers.append(s)
            lst_len = 0
            break

        lst_len += 1
        seen.append(s)

    if lst_len > best:
        best = lst_len
        best_lst = lst

print(best, best_lst)
print("smallest member of longest list", min(best_lst))
