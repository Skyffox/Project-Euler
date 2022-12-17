#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 41.py:

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    # Check only for odd numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    

def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]
    
    l = []
    for i in range(len(lst)):
        # Extract lst[i] from the list. remLst is remaining list
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

largest_prime = 0
for n in range(10):
    lst = list(range(1, n))
    permutation_lst = permutation(lst)
    for sub_lst in permutation_lst:
        num = int(''.join(map(str, sub_lst)))
        if is_prime(num):
            if num > largest_prime:
                largest_prime = num
            
print ("The largest n-digit pandigital prime is:", largest_prime)
