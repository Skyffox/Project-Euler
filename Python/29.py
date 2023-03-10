# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5
# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100
# and 2 ≤ b ≤ 100?
# Execution time: 0.225s

num_lst = []

for a in range(2, 101):
    for b in range(2, 101):
        num_lst.append(a**b)

s = sorted(set(num_lst))
print ("Amount of distinct numbers in the sequence:", len(s))
