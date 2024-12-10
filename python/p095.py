# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, 
# and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. 
# For this reason, 220 and 284 are called an amicable pair.
# Since this chain returns to its starting point, it is called an amicable chain.
# Find the smallest member of the longest amicable chain with no element exceeding one million.
# Execution time: 466.186s

def proper_divisors(n):
    i = 1
    lst = []
    # Note that this loop runs till square root
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
